from sqlalchemy.orm import Session

from app.crud.analyses import get_analyses_by_user
from app.crud.job_descriptions import get_job_descriptions_by_user
from app.crud.resumes import get_resumes_by_user
from app.crud.roadmaps import get_roadmaps_by_user

from app.services.document_ingestion import ingest_document

from app.services.formatters import (
    format_analysis_for_ingestion,
    format_roadmap_for_ingestion,
)


def reindex_user_documents(
    db: Session,
    user_id: int,
) -> dict:

    resumes = get_resumes_by_user(
        db=db,
        user_id=user_id,
    )

    for resume in resumes:

        ingest_document(
            db=db,
            user_id=user_id,
            source_type="resume",
            source_id=resume.id,
            content=resume.extracted_text or "",
        )

    job_descriptions = get_job_descriptions_by_user(
        db=db,
        user_id=user_id,
    )

    for job_description in job_descriptions:

        ingest_document(
            db=db,
            user_id=user_id,
            source_type="job_description",
            source_id=job_description.id,
            content=job_description.content,
        )

    analyses = get_analyses_by_user(
        db=db,
        user_id=user_id,
    )

    for analysis in analyses:

        analysis_text = format_analysis_for_ingestion(
            matched_skills=analysis.matched_skills,
            missing_skills=analysis.missing_skills,
            recommendations=analysis.recommendations,
        )

        ingest_document(
            db=db,
            user_id=user_id,
            source_type="analysis",
            source_id=analysis.id,
            content=analysis_text,
        )

    roadmaps = get_roadmaps_by_user(
        db=db,
        user_id=user_id,
    )

    for roadmap in roadmaps:

        roadmap_text = format_roadmap_for_ingestion(
            roadmap.content,
        )

        ingest_document(
            db=db,
            user_id=user_id,
            source_type="roadmap",
            source_id=roadmap.id,
            content=roadmap_text,
        )

    return {
        "resumes": len(resumes),
        "job_descriptions": len(job_descriptions),
        "analyses": len(analyses),
        "roadmaps": len(roadmaps),
    }