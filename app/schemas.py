from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.types import conint


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    created_at: datetime


class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(BasePost):
    pass


class Post(BasePost):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    owner_id: int
    owner: User


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Like(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)


class PostLike(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    Post: Post
    likes: int
