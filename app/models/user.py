from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    role: str = "user"
    created_at: datetime = Field(default_factory=datetime.utcnow)

    schemas: List["Schema"] = Relationship(back_populates="uploader")
