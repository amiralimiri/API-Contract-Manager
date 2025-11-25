from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from .schema_version import SchemaVersion


class Schema(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    current_version: Optional[int] = Field(
        default=None, foreign_key="schemaversion.version_id"
    )
    uploaded_by: Optional[int] = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    versions: list[SchemaVersion] = Relationship(back_populates="schema")
