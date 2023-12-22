"""create employees table

Revision ID: d9dba5ae0ed3
Revises: d1c4dcec7499
Create Date: 2023-12-22 14:49:39.543649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
# revision identifiers, used by Alembic.
revision: str = 'd9dba5ae0ed3'
down_revision: Union[str, None] = 'd1c4dcec7499'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "employees",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
        sa.Column("employee_name", sa.String(255), nullable=True),
        sa.Column("email", sa.String(255), nullable=True),
        sa.Column("mobile", sa.String(500), nullable=True),
        sa.Column("location", sa.String(255), nullable=True),
        sa.Column("state", sa.String(100), unique=False, nullable=True),
        sa.Column("city", sa.String(100), unique=False, nullable=True),
        sa.Column("pincode", sa.String(100), unique=False, nullable=True),
        sa.Column("education", sa.String(255), unique=False, nullable=True),
        sa.Column("experience", sa.String(255), unique=False, nullable=True),
        sa.Column("ctc", sa.String(255), unique=False, nullable=True),
        sa.Column("password_hash", sa.String(255), unique=False, nullable=True),
        sa.Column("role_type", sa.String(255), nullable=True),
        sa.Column("status", sa.Integer, server_default='0'),
    )


def downgrade() -> None:
    op.drop_table("employees")
