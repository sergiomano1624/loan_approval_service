"""create test table

Revision ID: cd23389661c8
Revises: 
Create Date: 2023-12-15 13:36:28.380577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from models.item import Item
from sqlalchemy import DateTime
from sqlalchemy.sql import func
# revision identifiers, used by Alembic.
revision: str = 'cd23389661c8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        Item.__tablename__,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), unique=True, nullable=False),
        sa.Column("description", sa.String(100), unique=True, nullable=False),
        sa.Column("created_by", sa.String(100), nullable=True),
        sa.Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
        sa.Column("updated_by", sa.String(100), nullable=True),
        sa.Column("updated_at", DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now(),
                  nullable=True),
        sa.Column("deleted_by", sa.String(100), nullable=True),
        sa.Column("deleted_at", DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    op.drop_table(Item.__tablename__)
