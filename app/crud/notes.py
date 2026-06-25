from sqlalchemy.orm import Session

from app.models import Note
def create_note(
    db: Session,
    user_id: int,
    title: str,
    content: str,
):
    note = Note(
        user_id=user_id,
        title=title,
        content=content,
    )

    db.add(note)
    db.commit()
    db.refresh(note)

    return note


def get_note_by_id(db:Session,note_id:int):
    return db.query(Note).filter(Note.id==note_id).first()


def get_notes_by_user(
    db: Session,
    user_id: int,
):
    return (
        db.query(Note)
        .filter(
            Note.user_id == user_id
        )
        .order_by(
            Note.updated_at.desc()
        )
        .all()
    )


def update_note(
    db: Session,
    note: Note,
    update_data: dict,
):
    for field, value in update_data.items():
        setattr(
            note,
            field,
            value,
        )

    db.commit()
    db.refresh(note)

    return note


def delete_note(
    db: Session,
    note: Note,
):
    db.delete(note)
    db.commit()