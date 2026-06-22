from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.document_ingestion import ingest_document
from app.services.formatters import (
    format_roadmap_for_ingestion,
)
from app.core import get_current_user
from app.crud import (
    create_roadmap,
    get_analysis_by_id,
)
from app.db import get_db
from app.models import User
from app.schemas import RoadmapResponse
from app.services.roadmap import generate_learning_roadmap

router = APIRouter(
    prefix="/roadmaps",
    tags=["Roadmaps"],
)


@router.post(
    "/{analysis_id}",
    response_model=RoadmapResponse,
    status_code=201,
)
def generate_roadmap(
    analysis_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    analysis = get_analysis_by_id(
        db,
        analysis_id,
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found",
        )

    if analysis.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    roadmap_content = generate_learning_roadmap(
        analysis.missing_skills,
    )

    roadmap=create_roadmap(
        db=db,
        user_id=current_user.id,
        analysis_id=analysis.id,
        content=roadmap_content.model_dump(),
    )
    roadmap_text = format_roadmap_for_ingestion(
        roadmap.content
    )
    ingest_document(
        db=db,
        user_id=current_user.id,
        source_type="roadmap",
        source_id=roadmap.id,
        content=roadmap_text,
    )
    return roadmap_content