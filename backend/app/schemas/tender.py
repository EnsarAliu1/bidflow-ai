from datetime import datetime
from uuid import UUID
from typing import Literal

from pydantic import BaseModel, Field


class TenderCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    organization: str = Field(min_length=2, max_length=150)
    deadline: datetime
    estimated_budget: int | None = Field(gt=0)


class TenderResponse(BaseModel):
    id: UUID
    title: str
    organization: str
    deadline: datetime
    estimated_budget: int | None
    status: Literal["draft"]
