from sqlalchemy.orm import Session

from app.models import Roadmap


def create_roadmap(
    db: Session,
    user_id: int,
    analysis_id: int,
    content: dict
):
    roadmap = Roadmap(
        user_id=user_id,
        analysis_id=analysis_id,
        content=content
    )

    db.add(roadmap)
    db.commit()
    db.refresh(roadmap)

    return roadmap