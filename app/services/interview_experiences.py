from sqlalchemy.orm import Session

from app.crud.interview_experiences import (
    create_interview_experience,
    update_interview_experience,
    delete_interview_experience,
)

from app.crud.documents import (
    delete_source_documents,
)

from app.services.document_ingestion import (
    ingest_document,
)

from app.services.formatters import (
    format_interview_experience_for_ingestion,
)



def create_interview_experience_service(
    db: Session,
    user_id: int,
    interview_data,
):
    interview = create_interview_experience(
        db=db,
        user_id=user_id,
        **interview_data.model_dump(),
    )

    interview_text = (
        format_interview_experience_for_ingestion(
            company=interview.company,
            role=interview.role,
            interview_type=interview.interview_type,
            outcome=interview.outcome,
            questions_asked=interview.questions_asked,
            experience=interview.experience,
            lessons_learned=interview.lessons_learned,
        )
    )

    ingest_document(
        db=db,
        user_id=user_id,
        source_type="interview_experience",
        source_id=interview.id,
        content=interview_text,
    )

    return interview


def update_interview_experience_service(
    db: Session,
    interview,
    update_data: dict,
):
    interview = update_interview_experience(
        db=db,
        interview=interview,
        update_data=update_data,
    )

    interview_text = (
        format_interview_experience_for_ingestion(
            company=interview.company,
            role=interview.role,
            interview_type=interview.interview_type,
            outcome=interview.outcome,
            questions_asked=interview.questions_asked,
            experience=interview.experience,
            lessons_learned=interview.lessons_learned,
        )
    )

    ingest_document(
        db=db,
        user_id=interview.user_id,
        source_type="interview_experience",
        source_id=interview.id,
        content=interview_text,
    )

    return interview



def delete_interview_experience_service(
    db: Session,
    interview,
):
    delete_source_documents(
        db=db,
        source_type="interview_experience",
        source_id=interview.id,
    )

    delete_interview_experience(
        db=db,
        interview=interview,
    )