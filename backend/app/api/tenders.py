from fastapi import APIRouter, status
from app.schemas.tender import TenderResponse, TenderCreate
from app.services.tender_service import TenderService

tender_service = TenderService()

router = APIRouter(
    prefix="/api/v1/tenders",
    tags=["Tenders"]
)


@router.post(
    "",
    response_model=TenderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_tender(data: TenderCreate):
    tender = tender_service.create_tender(data)
    return tender


@router.get(
    "",
    response_model=list[TenderResponse],
    status_code=status.HTTP_200_OK
)
def list_tenders():
    tenders = tender_service.list_tenders()
    return tenders
