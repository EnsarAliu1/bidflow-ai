from datetime import date
from uuid import UUID
from typing import Literal

from pydantic import BaseModel, Field, ConfigDict, model_validator
from app.domain.tender import TenderStatus


class TenderCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    organization: str = Field(min_length=2, max_length=150)
    deadline: date
    estimated_budget: int | None = Field(default=None, gt=0)


class TenderResponse(TenderCreate):
    id: UUID
    status: TenderStatus
    model_config = ConfigDict(from_attributes=True)


class TenderUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=200
    )

    organization: str | None = Field(
        default=None,
        min_length=2,
        max_length=150
    )

    deadline: date | None = Field(
        default=None
    )

    estimated_budget: int | None = Field(
        default=None,
        gt=0
    )

    @model_validator(mode="after")
    def reject_explicit_nulls(self) -> "TenderUpdate":
        for field in ("title", "organization", "deadline"):
            if field in self.model_fields_set and getattr(self, field) is None:
                raise ValueError(f"{field} cannot be null")

        return self


class TenderStatusUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: TenderStatus
