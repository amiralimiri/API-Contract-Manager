from datetime import datetime
from typing import Any, Dict, List, Optional

from sqlmodel import JSON, Field, Relationship, SQLModel


# ----------------------
# User
# ----------------------
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    role: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    schemas: List["Schema"] = Relationship(back_populates="uploader")


# ----------------------
# SchemaVersion
# ----------------------
class SchemaVersion(SQLModel, table=True):
    version_id: Optional[int] = Field(default=None, primary_key=True)

    schema_id: int = Field(foreign_key="schema.id")
    version_number: int
    file_path: str
    diff_summary: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    schema: "Schema" = Relationship(back_populates="versions")


# ----------------------
# Schema
# ----------------------
class Schema(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    current_version: Optional[int] = Field(
        default=None, foreign_key="schemaversion.version_id"
    )
    uploaded_by: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    versions: List[SchemaVersion] = Relationship(back_populates="schema")
    uploader: User = Relationship(back_populates="schemas")
    notifications: List["Notification"] = Relationship(back_populates="schema")


# ----------------------
# Notification
# ----------------------
class Notification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    schema_id: int = Field(foreign_key="schema.id")
    event_type: str
    payload: Dict[str, Any] = Field(
        sa_column=Field(default={}, sa_column_kwargs={"type_": JSON})
    )
    sent_at: datetime = Field(default_factory=datetime.utcnow)

    schema: Schema = Relationship(back_populates="notifications")
