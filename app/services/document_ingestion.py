from sqlalchemy.orm import Session

from app.crud.documents import (
    create_document,
    delete_source_documents,
)
from app.services.chunking import chunk_text
from app.services.embeddings import generate_embedding


def ingest_document(
    db: Session,
    user_id: int,
    source_type: str,
    source_id: int,
    content: str,
) -> None:

    if not content.strip():
        return

    delete_source_documents(
        db=db,
        source_type=source_type,
        source_id=source_id,
    )

    chunks = chunk_text(content)

    for chunk in chunks:

        embedding = generate_embedding(chunk)

        create_document(
            db=db,
            user_id=user_id,
            source_type=source_type,
            source_id=source_id,
            content=chunk,
            embeddings=embedding,
        )

    db.commit()