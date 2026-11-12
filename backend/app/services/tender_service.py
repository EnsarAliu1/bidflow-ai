from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.tender import Tender
from app.schemas.tender import TenderCreate, TenderUpdate
from app.domain.tender import TenderStatus, can_transaction
from app.core.exceptions import TenderNotFoundError, TenderConflictError

from uuid import UUID


class TenderService:

    def __init__(self, db: Session):
        self.db = db

    def _get_tender_for_update(self, tender_id: UUID) -> Tender:
        statement = (
            select(Tender)
            .where(Tender.id == tender_id)
            .with_for_update()
            .execution_options(populate_existing=True)
        )

        tender = self.db.scalars(statement).one_or_none()

        if tender is None:
            raise TenderNotFoundError()

        return tender

    def create_tender(self, data: TenderCreate) -> Tender:
        tender = Tender(
            **data.model_dump(),
            status="draft",
        )

        try:
            self.db.add(tender)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

        self.db.refresh(tender)
        return tender

    def list_tenders(self) -> list[Tender]:
        return list(self.db.scalars(select(Tender)).all())

    def get_tender(
            self,
            tender_id: UUID
    ) -> Tender:
        tender = self.db.get(Tender, tender_id)

        if not tender:
            raise TenderNotFoundError

        return tender

    def update_tender(
            self,
            tender_id: UUID,
            data: TenderUpdate,
    ) -> Tender:
        try:
            tender = self._get_tender_for_update(tender_id)

            if tender.status not in (
                TenderStatus.DRAFT,
                TenderStatus.IN_REVIEW,
            ):
                raise TenderConflictError(
                    "Tender cannot be updated in its current status"
                )

            updates = data.model_dump(exclude_unset=True)

            for field, value in updates.items():
                setattr(tender, field, value)

            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

        self.db.refresh(tender)
        return tender

    def update_status(
            self,
            tender_id: UUID,
            target: TenderStatus
    ) -> Tender:
        try:
            tender = self._get_tender_for_update(tender_id)

            current = TenderStatus(tender.status)

            if not can_transaction(current, target):
                raise TenderConflictError(
                    f"Cannot change status from {current.value}"
                    f"to {target.value}"
                )

            tender.status = target.value
            self.db.commit()

        except Exception:
            self.db.rollback()
            raise

        self.db.refresh(tender)
        return tender

    def delete_tender(
            self,
            tender_id: UUID,
    ) -> None:
        try:
            tender = self._get_tender_for_update(tender_id)

            if tender.status != TenderStatus.DRAFT:
                raise TenderConflictError()

            self.db.delete(tender)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
