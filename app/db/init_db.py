# app/db/init_db.py
from sqlmodel import SQLModel

from app.db.session import engine


def init_db():
    from app.db.base import metadata

    SQLModel.metadata.create_all(engine)
