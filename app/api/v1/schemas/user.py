from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    role: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
