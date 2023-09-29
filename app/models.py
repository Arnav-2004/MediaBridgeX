from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    content = Column(String(3000), nullable=False)
    published = Column(Boolean, server_default='1', nullable=False)
    created_at = Column(TIMESTAMP(True), server_default=text("now()"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False)
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(320), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    created_at = Column(TIMESTAMP(True), server_default=text("now()"), nullable=False)


class Like(Base):
    __tablename__ = "likes"

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="cascade"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), primary_key=True)
