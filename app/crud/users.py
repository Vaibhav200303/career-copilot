from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.models import User


def get_user_by_email(
    db: Session,
    email: EmailStr
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(
    db: Session,
    user: dict
):
    existing = (
        db.query(User)
        .filter(User.email == user["email"])
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    db_user = User(**user)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user