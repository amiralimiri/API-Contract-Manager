from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class SchemaVersion(SQLModel, table=True):
    version_id: Optional[int] = Field(default=None, primary_key=True)
    schema_id: int = Field(foreign_key="schema.id")
    version_number: int
    file_path: str
    diff_summary: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    schema: "Schema" = Relationship(back_populates="versions")
