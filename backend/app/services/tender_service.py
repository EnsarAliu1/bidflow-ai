from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.tender import Tender
from app.schemas.tender import TenderCreate


class TenderService:

    def __init__(self, db: Session):
        self.db = db

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
