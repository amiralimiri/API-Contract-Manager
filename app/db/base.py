# app/db/base.py
from sqlmodel import SQLModel

from app.models.notification import Notification
from app.models.schema import Schema
from app.models.schema_version import SchemaVersion

# تمام مدل‌های پروژه باید اینجا import شوند تا Alembic آنها را بشناسد
from app.models.user import User

# متادیتای اصلی برای Alembic
metadata = SQLModel.metadata
