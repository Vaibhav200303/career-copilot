from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.crud.conversations import (
    create_conversation,
    get_conversation_by_id_and_user,
)
from app.crud.chat_messages import create_chat_message
from app.crud.chat_messages import get_recent_messages
from app.crud.conversations import (
    update_last_message_time,
)

from app.services.retrieval import (
    retrieve_relevant_chunks,
)

from app.services.rag import (
    build_rag_prompt,
    generate_rag_response,
)
from app.core.constants import MAX_CONVERSATION_TITLE_LENGTH
def get_or_create_conversation(
    db: Session,
    user_id: int,
    conversation_id: int | None,
    first_message: str,
):
    if conversation_id:

        conversation = get_conversation_by_id_and_user(
            db=db,
            conversation_id=conversation_id,
            user_id=user_id,
        )

        if not conversation:
            raise HTTPException(
                status_code=404,
                detail="Conversation not found",
            )

        return conversation

    title = first_message.strip()

    if len(title) > MAX_CONVERSATION_TITLE_LENGTH:
        title = title[:MAX_CONVERSATION_TITLE_LENGTH].rstrip() + "..."

    conversation = create_conversation(
        db=db,
        user_id=user_id,
        title=title,
    )

    return conversation


def save_user_message(
    db: Session,
    conversation_id: int,
    message: str,
):
    return create_chat_message(
        db=db,
        conversation_id=conversation_id,
        role="user",
        content=message,
    )

def save_assistant_message(
    db: Session,
    conversation_id: int,
    message: str,
):
    return create_chat_message(
        db=db,
        conversation_id=conversation_id,
        role="assistant",
        content=message,
    )


def get_chat_history(
    db: Session,
    conversation_id: int,
):
    return get_recent_messages(
        db=db,
        conversation_id=conversation_id,
        limit=10,
    )


def chat(
    db: Session,
    user_id: int,
    conversation_id: int | None,
    message: str,
):
    conversation = get_or_create_conversation(
        db=db,
        user_id=user_id,
        conversation_id=conversation_id,
        first_message=message,
    )
    save_user_message(
        db=db,
        conversation_id=conversation.id,
        message=message,
    )
    history = get_chat_history(
        db=db,
        conversation_id=conversation.id,
    )
    chunks = retrieve_relevant_chunks(
        db=db,
        user_id=user_id,
        query=message,
    )
    prompt = build_rag_prompt(
        chunks=chunks,
        question=message,
        chat_history=history,
    )
    answer = generate_rag_response(prompt)
    save_assistant_message(
        db=db,
        conversation_id=conversation.id,
        message=answer,
    )
    update_last_message_time(
        db=db,
        conversation=conversation,
    )
    return {
        "conversation_id": conversation.id,
        "title":conversation.title,
        "message": answer,
    }