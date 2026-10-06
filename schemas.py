from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints


class RegisterRequest(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]
    email: EmailStr
    password: str = Field(min_length=6)


class LoginRequest(BaseModel):
    email: str
    password: str


class ProfileResponse(BaseModel):
    name: str
    email: str
