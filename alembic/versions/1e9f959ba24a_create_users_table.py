"""create users table

Revision ID: 1e9f959ba24a
Revises: cd23389661c8
Create Date: 2023-12-19 10:42:30.457339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models.Users import Users
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

# revision identifiers, used by Alembic.
revision: str = '1e9f959ba24a'
down_revision: Union[str, None] = 'cd23389661c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        Users.__tablename__,
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
        sa.Column("first_name", sa.String(255), nullable=True),
        sa.Column("last_name", sa.String(255), nullable=True),
        sa.Column("password", sa.String(500), nullable=True),
        sa.Column("gender", sa.String(100), nullable=True),
        sa.Column("email", sa.String(100), unique=False, nullable=True),
        sa.Column("mobile", sa.String(100), unique=False, nullable=True),
        sa.Column("user_type", sa.String(255), nullable=False),
        sa.Column("status", sa.Integer, server_default='0'),
        sa.Column("last_login", DateTime(timezone=True), nullable=True),
        sa.Column("token", sa.String(255), nullable=True),
        sa.Column("expired_at", sa.String(255), nullable=True),
        sa.Column("created_by", sa.String(100), nullable=True),
        sa.Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
        sa.Column("updated_by", sa.String(100), nullable=True),
        sa.Column("updated_at", DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now(),
                  nullable=True),
        sa.Column("deleted_by", sa.String(100), nullable=True),
        sa.Column("deleted_at", DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    op.drop_table(Users.__tablename__)
