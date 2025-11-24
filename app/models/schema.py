from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from .schema_version import SchemaVersion
from .user import User


class Schema(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    current_version: Optional[int] = Field(
        default=None, foreign_key="schemaversions.version_id"
    )
    uploaded_by: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    uploader: Optional[User] = Relationship(back_populates="schemas")
    versions: list["SchemaVersion"] = Relationship(back_populates="schema")
