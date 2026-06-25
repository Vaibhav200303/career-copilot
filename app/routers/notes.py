from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core import get_current_user
from app.db import get_db
from fastapi import HTTPException
from app.models import User
from app.crud.notes import (
    get_notes_by_user,
    get_note_by_id
)
from app.schemas.note import (
    NoteCreate,
    NoteResponse,
    NoteUpdate
)
from app.services.notes import (
    update_note_service,
    create_note_service,
    delete_note_service
)

router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)


@router.post(
    "",
    response_model=NoteResponse,
    status_code=201,
)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_note_service(
        db=db,
        user_id=current_user.id,
        title=note.title,
        content=note.content,
    )

@router.get(
    "",
    response_model=list[NoteResponse],
)
def get_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_notes_by_user(
        db=db,
        user_id=current_user.id,
    )


@router.get(
    "/{note_id}",
    response_model=NoteResponse,
)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = get_note_by_id(
        db=db,
        note_id=note_id,
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        )

    if note.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    return note


@router.put(
    "/{note_id}",
    response_model=NoteResponse,
)
def update_note(
    note_id: int,
    note_data: NoteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = get_note_by_id(
        db=db,
        note_id=note_id,
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        )

    if note.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    return update_note_service(
        db=db,
        note=note,
        note_data=note_data
    )

@router.delete(
    "/{note_id}",
)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = get_note_by_id(
        db=db,
        note_id=note_id,
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        )

    if note.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    delete_note_service(
        db=db,
        note=note,
    )

    return {
        "message": "Note deleted successfully"
    }