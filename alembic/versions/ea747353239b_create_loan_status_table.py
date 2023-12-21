"""create loan_status table

Revision ID: ea747353239b
Revises: d1c4dcec7499
Create Date: 2023-12-21 14:07:33.762804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from models.LoanStatus import LoanStatus
from sqlalchemy import DateTime
from sqlalchemy.sql import func
# revision identifiers, used by Alembic.
revision: str = 'ea747353239b'
down_revision: Union[str, None] = 'd1c4dcec7499'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        LoanStatus.__tablename__,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("application_id", sa.Integer, index=True),
        sa.Column("date", sa.String(255), nullable=True),
        sa.Column("amount_offered", sa.String(255), nullable=True),
        sa.Column("type", sa.String(255), nullable=True),
        sa.Column("comments", sa.String(255), nullable=True),
        sa.Column("status", sa.String(255), nullable=True),
        sa.Column("created_by", sa.String(100), nullable=True),
        sa.Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
        sa.Column("updated_by", sa.String(100), nullable=True),
        sa.Column("updated_at", DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now(),
                  nullable=True),
        sa.Column("deleted_by", sa.String(100), nullable=True),
        sa.Column("deleted_at", DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    op.drop_table(LoanStatus.__tablename__)
