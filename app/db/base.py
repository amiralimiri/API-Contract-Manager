# app/db/base.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.notification import Notification
from app.models.schema import Schema
from app.models.schema_version import SchemaVersion

# این بخش بسیار مهم است: مدل‌ها باید import شوند
# تا Alembic بتواند آن‌ها را پیدا کند.
from app.models.user import User
