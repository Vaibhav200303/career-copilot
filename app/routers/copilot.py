from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core import get_current_user
from app.db import get_db
from app.models import User
from app.schemas import ChatRequest,ChatResponse
from app.services.conversations import chat


router=APIRouter(prefix="/copilot",tags=["Career Copilot"])

@router.post("/chat",response_model=ChatResponse)
def copilot_chat(request:ChatRequest,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return chat(db=db,user_id=current_user.id,conversation_id=request.conversation_id,message=request.message)