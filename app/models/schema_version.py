from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, JSON
from sqlmodel import Field, Relationship, SQLModel


class SchemaVersion(SQLModel, table=True):
    version_id: Optional[int] = Field(default=None, primary_key=True)
    schema_id: int = Field(foreign_key="schema.id")
    version_number: int
    file_path: str
    schema_body: dict | None = Field(default=None, sa_column=Column(JSON))
    diff_summary: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    schema: "Schema" = Relationship(back_populates="versions")
