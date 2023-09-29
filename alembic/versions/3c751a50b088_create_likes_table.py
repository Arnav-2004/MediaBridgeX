"""Create likes table

Revision ID: 3c751a50b088
Revises: 11acf7c67880
Create Date: 2023-09-29 17:51:39.576051

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c751a50b088'
down_revision: Union[str, None] = '11acf7c67880'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("likes", sa.Column("post_id", sa.Integer, sa.ForeignKey("posts.id", ondelete="cascade"), primary_key=True), sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="cascade"), primary_key=True))


def downgrade() -> None:
    op.drop_table("likes")
