from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.core import get_current_user
from app.db import get_db
from app.models import User

from app.schemas import (
    ConversationResponse,
    ConversationDetailResponse,
)

from app.crud.conversations import (
    get_conversation_by_id_and_user,
    get_conversations_by_user,
    delete_conversation,
)

from app.crud.chat_messages import (
    get_messages_by_conversation,
)

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)
@router.get(
    "",
    response_model=list[ConversationResponse],
)
def get_conversations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_conversations_by_user(
        db=db,
        user_id=current_user.id,
    )


@router.get(
    "/{conversation_id}",
    response_model=ConversationDetailResponse,
)
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    conversation = get_conversation_by_id_and_user(
        db=db,
        conversation_id=conversation_id,
        user_id=current_user.id,
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    messages = get_messages_by_conversation(
        db=db,
        conversation_id=conversation.id,
    )

    return ConversationDetailResponse(
        id=conversation.id,
        title=conversation.title,
        created_at=conversation.created_at,
        updated_at=conversation.updated_at,
        last_message_at=conversation.last_message_at,
        messages=messages,
    )
@router.delete(
    "/{conversation_id}",
)
def remove_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    conversation = get_conversation_by_id_and_user(
        db=db,
        conversation_id=conversation_id,
        user_id=current_user.id,
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    delete_conversation(
        db=db,
        conversation=conversation,
    )

    return {
        "message": "Conversation deleted successfully"
    }