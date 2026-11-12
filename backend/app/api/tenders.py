from fastapi import APIRouter, status, Depends
from app.schemas.tender import TenderResponse, TenderCreate
from app.services.tender_service import TenderService

from typing import Annotated
from sqlalchemy.orm import Session

from app.db.session import get_db


router = APIRouter(
    prefix="/api/v1/tenders",
    tags=["Tenders"]
)


@router.post(
    "",
    response_model=TenderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_tender(
    data: TenderCreate,
    db: Annotated[Session, Depends(get_db)],
):
    service = TenderService(db)
    return service.create_tender(data)


@router.get(
    "",
    response_model=list[TenderResponse],
    status_code=status.HTTP_200_OK
)
def list_tenders(
    db: Annotated[Session, Depends(get_db)],
):
    service = TenderService(db)
    return service.list_tenders()
