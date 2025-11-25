from sqlmodel import SQLModel

from app.models.models import Notification, Schema, SchemaVersion, User  # noqa: F401

# متادیتای اصلی برای Alembic
metadata = SQLModel.metadata
