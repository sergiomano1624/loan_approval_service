"""create documents table

Revision ID: d1c4dcec7499
Revises: b25983144d01
Create Date: 2023-12-21 09:37:20.884892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from models.Documents import Documents
from sqlalchemy import DateTime
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision: str = 'd1c4dcec7499'
down_revision: Union[str, None] = 'b25983144d01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        Documents.__tablename__,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("bank_account_id", sa.Integer, index=True),
        sa.Column("public_id", sa.String(255), nullable=True),
        sa.Column("secure_url", sa.String(255), nullable=True),
        sa.Column("created_by", sa.String(100), nullable=True),
        sa.Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
        sa.Column("updated_by", sa.String(100), nullable=True),
        sa.Column("updated_at", DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now(),
                  nullable=True),
        sa.Column("deleted_by", sa.String(100), nullable=True),
        sa.Column("deleted_at", DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    op.drop_table(Documents.__tablename__)
