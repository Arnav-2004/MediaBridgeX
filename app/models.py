from datetime import datetime
from typing_extensions import Annotated
from typing import List
from sqlalchemy import Boolean, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]
users_fk = Annotated[int, mapped_column(ForeignKey("users.id", ondelete="cascade"))]
users_pk_fk = Annotated[
    int, mapped_column(ForeignKey("users.id", ondelete="cascade"), primary_key=True)
]
posts_pk_fk = Annotated[
    int, mapped_column(ForeignKey("posts.id", ondelete="cascade"), primary_key=True)
]


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(300))
    content: Mapped[str] = mapped_column(String(3000))
    published: Mapped[bool] = mapped_column(Boolean, server_default="1")
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(True), server_default=text("now()")
    )
    owner_id: Mapped[users_fk]
    owner: Mapped[List["User"]] = relationship("User")


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(String(320), unique=True)
    password: Mapped[str] = mapped_column(String(256))
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(True), server_default=text("now()")
    )


class Like(Base):
    __tablename__ = "likes"

    post_id: Mapped[posts_pk_fk]
    user_id: Mapped[users_pk_fk]
