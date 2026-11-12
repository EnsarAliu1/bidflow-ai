from fastapi import APIRouter, status, Depends
from app.schemas.tender import TenderResponse, TenderCreate, TenderStatusUpdate, TenderUpdate, TenderStatus
from app.services.tender_service import TenderService

from typing import Annotated
from sqlalchemy.orm import Session

from app.db.session import get_db

from uuid import UUID


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


@router.get(
    "/{tender_id}",
    response_model=TenderResponse
)
def get_tender(
    tender_id: UUID,
    db: Annotated[Session, Depends(get_db)],
):
    service = TenderService(db)
    return service.get_tender(tender_id)


@router.patch(
    "/{tender_id}",
    response_model=TenderResponse
)
def update_tender(
    tender_id: UUID,
    data: TenderUpdate,
    db: Annotated[Session, Depends(get_db)]
):
    service = TenderService(db)
    return service.update_tender(tender_id, data)


@router.patch(
    "/{tender_id}/status",
    response_model=TenderResponse
)
def update_tender_status(
    tender_id: UUID,
    data: TenderStatusUpdate,
    db: Annotated[Session, Depends(get_db)],
):
    service = TenderService(db)
    return service.update_status(
        tender_id,
        data.status,
    )


@router.delete(
    "/{tender_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_tender(
    tender_id: UUID,
    db: Annotated[Session, Depends(get_db)]
):
    service = TenderService(db)
    return service.delete_tender(tender_id)
