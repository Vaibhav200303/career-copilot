from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core import get_current_user
from app.db import get_db
from app.models import User
from app.schemas import ChatRequest,ChatResponse
from app.services.retrieval import retrieve_relevant_chunks
from app.services.rag import build_rag_prompt,generate_rag_response

router=APIRouter(prefix="/copilot",tags=["Career Copilot"])

@router.post("/chat",response_model=ChatResponse)
def chat(request:ChatRequest,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    chunks=retrieve_relevant_chunks(
        db=db,
        user_id=current_user.id,
        query=request.message,
        top_k=3
    )
    prompt=build_rag_prompt(
        chunks=chunks,
        question=request.message
    )
    answer=generate_rag_response(
        prompt=prompt
    )
    return ChatResponse(message=answer)