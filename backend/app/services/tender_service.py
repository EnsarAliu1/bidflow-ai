from uuid import UUID, uuid4

from app.schemas.tender import TenderCreate, TenderResponse

_tenders: dict[UUID, TenderResponse] = {}


class TenderService:
    def create_tender(self, data: TenderCreate) -> TenderResponse:
        tender_id = uuid4()

        tender = TenderResponse(
            **data.model_dump(),
            id=tender_id,
            status="draft",
        )

        _tenders[tender_id] = tender
        return tender

    def list_tenders(self) -> list[TenderResponse]:
        return list(_tenders.values())
