"""Create users table

Revision ID: 7fc1834de126
Revises: 9a50b72bb6c9
Create Date: 2023-09-29 17:27:19.253398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7fc1834de126"
down_revision: Union[str, None] = "9a50b72bb6c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(320), unique=True, nullable=False),
        sa.Column("password", sa.String(256), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("users")
