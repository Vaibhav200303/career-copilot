from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core import get_current_user
from app.db import get_db
from app.models import User

from app.services.reindex import (
    reindex_user_documents,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post("/reindex")
def reindex_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    result = reindex_user_documents(
        db=db,
        user_id=current_user.id,
    )

    return {
        "status": "success",
        **result,
    }