from datetime import datetime

from sqlalchemy.orm import Session

from app.models import Conversation

def create_conversation(
    db: Session,
    user_id: int,
    title: str,
):
    conversation = Conversation(
        user_id=user_id,
        title=title,
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation

def get_conversation_by_id_and_user(
    db: Session,
    conversation_id: int,
    user_id:int
):
    return (
        db.query(Conversation)
        .filter(
            Conversation.id == conversation_id,
            Conversation.user_id==user_id,
        )
        .first()
    )

def get_conversations_by_user(
    db: Session,
    user_id: int,
):
    return (
        db.query(Conversation)
        .filter(
            Conversation.user_id == user_id
        )
        .order_by(
            Conversation.last_message_at.desc()
        )
        .all()
    )


def update_conversation_title(
    db: Session,
    conversation: Conversation,
    title: str,
):
    conversation.title = title

    db.commit()
    db.refresh(conversation)

    return conversation

def update_last_message_time(
    db: Session,
    conversation: Conversation,
):
    conversation.last_message_at = datetime.utcnow()

    db.commit()
    db.refresh(conversation)

    return conversation


def delete_conversation(
    db: Session,
    conversation: Conversation,
):
    db.delete(conversation)
    db.commit()