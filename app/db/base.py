from sqlmodel import SQLModel

from app.models.schema import Schema  # noqa: F401
from app.models.schema_version import SchemaVersion  # noqa: F401
from app.models.user import User  # noqa: F401

metadata = SQLModel.metadata
