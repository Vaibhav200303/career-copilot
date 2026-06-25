from datetime import datetime

from pydantic import BaseModel

from app.schemas import ChatMessageResponse


class ConversationResponse(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
    last_message_at: datetime

    model_config = {
        "from_attributes": True
    }


class ConversationDetailResponse(
    ConversationResponse
):
    messages: list[ChatMessageResponse]