from pydantic import BaseModel, HttpUrl, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    email: EmailStr
    name: str
    password: str

class UserSchema(UserBase):
    email: EmailStr
    name: str
    password: str = Field(min_length=8)

class UserResponse(UserBase):
    id: UUID
    name: str
    email: EmailStr
    class Config:
        from_attributes = True


class LinkBase(BaseModel):
    original_link: HttpUrl
    privacy: Optional[str] = Field(default="public", pattern="^(public|private)$")

class LinkCreate(LinkBase):
    expiresAt: Optional[datetime] = None

class LinkSchema(BaseModel):
    id: UUID
    original_link: HttpUrl
    shortened_link: HttpUrl
    expiresAt: Optional[datetime] = None
    createdAt: datetime
    visitCount: int
    owner: List[UserResponse] = []

    class Config:
        from_attributes = True