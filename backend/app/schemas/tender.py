from datetime import date
from uuid import UUID
from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


class TenderCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    organization: str = Field(min_length=2, max_length=150)
    deadline: date
    estimated_budget: int | None = Field(default=None, gt=0)


class TenderResponse(TenderCreate):
    id: UUID
    status: Literal["draft"]
    model_config = ConfigDict(from_attributes=True)
