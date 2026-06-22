from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core import (
    authenticate_user,
    create_access_token,
    get_current_user,
    hash_password,
)
from app.crud import create_user
from app.db import get_db
from app.models import User
from app.schemas import Token, UserCreate, UserResponse

router = APIRouter(tags=["Authentication"])


@router.post("/users", response_model=UserResponse, status_code=201)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    user_data = user.model_dump()
    user_data["hashed_password"] = hash_password(
        user_data.pop("password")
    )

    return create_user(db, user_data)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(
        db,
        form_data.username,
        form_data.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user