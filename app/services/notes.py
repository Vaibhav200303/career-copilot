from sqlalchemy.orm import Session

from app.crud.notes import create_note,update_note,delete_note
from app.services.document_ingestion import (
    ingest_document,
)
from app.crud.documents import delete_source_documents
from app.models import Note
from app.schemas import NoteUpdate
def create_note_service(
    db: Session,
    user_id: int,
    title: str,
    content: str,
):
    note = create_note(
        db=db,
        user_id=user_id,
        title=title,
        content=content,
    )

    note_text = f"""
Title:
{note.title}

Content:
{note.content}
"""

    ingest_document(
        db=db,
        user_id=user_id,
        source_type="note",
        source_id=note.id,
        content=note_text,
    )

    return note


def update_note_service(
    db: Session,
    note:Note,
    note_data:dict
):
    updated_note = update_note(
        db=db,
        note=note,
        update_data=note_data.model_dump(exclude_unset=True)
    )

    note_text = f"""
Title:
{updated_note.title}

Content:
{updated_note.content}
"""

    ingest_document(
        db=db,
        user_id=updated_note.user_id,
        source_type="note",
        source_id=updated_note.id,
        content=note_text,
    )

    return updated_note


def delete_note_service(
    db: Session,
    note,
):
    delete_source_documents(
        db=db,
        source_type="note",
        source_id=note.id,
    )

    delete_note(
        db=db,
        note=note,
    )