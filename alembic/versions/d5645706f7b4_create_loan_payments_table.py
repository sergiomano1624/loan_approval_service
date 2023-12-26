"""create loan_payments table

Revision ID: d5645706f7b4
Revises: d9dba5ae0ed3
Create Date: 2023-12-26 12:36:52.864706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from models.LoanPayments import LoanPayments
from sqlalchemy import DateTime
from sqlalchemy.sql import func
# revision identifiers, used by Alembic.
revision: str = 'd5645706f7b4'
down_revision: Union[str, None] = 'd9dba5ae0ed3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        LoanPayments.__tablename__,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("loan_application_id", sa.Integer, index=True),
        sa.Column("payment_date", sa.String(255), nullable=True),
        sa.Column("principal", sa.String(255), nullable=True),
        sa.Column("interest", sa.String(255), nullable=True),
        sa.Column("amount", sa.String(255), unique=False, nullable=True),
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
    op.drop_table(LoanPayments.__tablename__)
