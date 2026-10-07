from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class User(BaseModel):
    name: str
    email: str


class UserCreate(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]
    email: EmailStr
    password: str = Field(min_length=6)


class UserInDB(User):
    hashed_password: str
