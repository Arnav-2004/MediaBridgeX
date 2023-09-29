"""Create posts table

Revision ID: 9a50b72bb6c9
Revises: 
Create Date: 2023-09-29 17:06:39.120023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a50b72bb6c9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer, primary_key=True), sa.Column("title", sa.String(300), nullable=False), sa.Column("content", sa.String(3000), nullable=False), sa.Column("published", sa.Boolean, server_default='1', nullable=False), sa.Column("created_at", sa.TIMESTAMP(True), server_default=sa.text("now()"), nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
