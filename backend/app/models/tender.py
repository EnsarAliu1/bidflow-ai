from datetime import date
from uuid import UUID, uuid4

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Date,
    String,
    Uuid
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Tender(Base):
    __tablename__ = "tenders"

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid4
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    organization: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    deadline: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    estimated_budget: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="draft",
        nullable=False,
    )

    __table_args__ = (
        CheckConstraint(
            "estimated_budget > 0",
            name="ck_tenders_positive_budget",
        ),
        CheckConstraint(
            "status = 'draft'",
            name="ck_tenders_draft_status_phase",
        ),
    )
