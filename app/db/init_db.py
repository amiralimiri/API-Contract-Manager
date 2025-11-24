# app/db/init_db.py
from sqlalchemy.orm import Session

from app.models.user import User


def init_db(db: Session):
    # نمونه: اگر خواستیم کاربر پیش‌فرض بسازیم
    existing = db.query(User).first()
    if not existing:
        user = User(email="admin@example.com")
        db.add(user)
        db.commit()
