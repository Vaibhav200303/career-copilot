from sqlalchemy.orm import Session

from app.models import ChatMessage

def create_chat_message(
    db: Session,
    conversation_id: int,
    role: str,
    content: str,
):
    message = ChatMessage(
        conversation_id=conversation_id,
        role=role,
        content=content,
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message

def get_recent_messages(
    db: Session,
    conversation_id: int,
    limit: int = 10,
):
    messages = (
        db.query(ChatMessage)
        .filter(
            ChatMessage.conversation_id == conversation_id
        )
        .order_by(
            ChatMessage.created_at.desc()
        )
        .limit(limit)
        .all()
    )

    return list(reversed(messages))


def get_messages_by_conversation(
    db: Session,
    conversation_id: int,
):
    return (
        db.query(ChatMessage)
        .filter(
            ChatMessage.conversation_id == conversation_id
        )
        .order_by(
            ChatMessage.created_at
        )
        .all()
    )