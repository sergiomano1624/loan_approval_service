"""create applications table

Revision ID: 0ab1bf29094a
Revises: 1e9f959ba24a
Create Date: 2023-12-20 13:20:41.274277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from models.Applications import Applications
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

# revision identifiers, used by Alembic.
revision: str = '0ab1bf29094a'
down_revision: Union[str, None] = '1e9f959ba24a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        Applications.__tablename__,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("borrower_name", sa.String(255), nullable=True),
        sa.Column("email", sa.String(255), nullable=True),
        sa.Column("address", sa.String(500), nullable=True),
        sa.Column("mobile", sa.String(100), nullable=True),
        sa.Column("dob", sa.String(100), unique=False, nullable=True),
        sa.Column("gender", sa.String(100), unique=False, nullable=True),
        sa.Column("credit_product", sa.String(255), unique=False, nullable=True),
        sa.Column("loan_amount", sa.BIGINT(), unique=False, nullable=True),
        sa.Column("term", sa.BIGINT(), unique=False, nullable=True),
        sa.Column("interest", sa.BIGINT(), unique=False, nullable=True),
        sa.Column("repayment_period", sa.BIGINT(), unique=False, nullable=True),
        sa.Column("trn_no", sa.String(255), nullable=False),
        sa.Column("monthly_income", sa.BIGINT(), nullable=False),
        sa.Column("public_id", sa.String(255), nullable=True),
        sa.Column("secure_url", sa.String(255), nullable=True),
        sa.Column("date", sa.String(255), nullable=True),
        sa.Column("amount_offered", sa.BIGINT(), server_default="0", nullable=True),
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
    op.drop_table(Applications.__tablename__)
