"""create bank_accounts table

Revision ID: b25983144d01
Revises: 0ab1bf29094a
Create Date: 2023-12-21 08:43:21.648541

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from models.BankAccounts import BankAccounts
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
# revision identifiers, used by Alembic.
revision: str = 'b25983144d01'
down_revision: Union[str, None] = '0ab1bf29094a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        BankAccounts.__tablename__,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("application_id", sa.Integer, index=True),
        sa.Column("bank_name", sa.String(255), nullable=True),
        sa.Column("bank_code", sa.String(255), nullable=True),
        sa.Column("bank_account_no", sa.String(255), nullable=True),
        sa.Column("bank_account_type", sa.String(255), unique=False, nullable=True),
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
    op.drop_table(BankAccounts.__tablename__)
