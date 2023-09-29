from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(BasePost):
    pass


class Post(BasePost):
    id: int
    created_at: datetime
    owner_id: int
    owner: User

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Like(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)


class PostLike(BaseModel):
    Post: Post
    likes: int

    class Config:
        from_attributes = True
