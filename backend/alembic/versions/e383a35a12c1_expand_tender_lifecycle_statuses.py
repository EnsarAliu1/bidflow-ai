"""expand tender lifecycle statuses

Revision ID: e383a35a12c1
Revises: 8f1db24a1684
Create Date: 2026-11-12 16:45:58.979967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e383a35a12c1'
down_revision: Union[str, Sequence[str], None] = '8f1db24a1684'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "ck_tenders_draft_status_phase",
        "tenders",
        type_="check",
    )

    op.create_check_constraint(
        "ck_tenders_valid_status",
        "tenders",
        "status IN ('draft', 'in_review', 'ready', 'submitted', 'won', 'lost')",
    )

    op.alter_column(
        "tenders",
        "status",
        existing_type=sa.String(),
        type_=sa.String(length=20),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "tenders",
        "status",
        existing_type=sa.String(length=20),
        type_=sa.String(),
        existing_nullable=False,
    )

    op.drop_constraint(
        "ck_tenders_valid_status",
        "tenders",
        type_="check",
    )

    op.create_check_constraint(
        "ck_tenders_draft_status_phase",
        "tenders",
        "status = 'draft'",
    )
