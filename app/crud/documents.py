from sqlalchemy.orm import Session
from app.models.document import Document

def create_document(
        db:Session,
        user_id:int,
        source_type:str,
        source_id:int,
        content:str,
        embeddings:list[float]
)->Document:
    document=Document(
        user_id=user_id,
        source_type=source_type,
        source_id=source_id,
        content=content,
        embedding=embeddings
    )
    db.add(document)
    return document

def delete_source_documents(
    db: Session,
    source_type: str,
    source_id: int,
) -> None:

    db.query(Document).filter(
        Document.source_type == source_type,
        Document.source_id == source_id,
    ).delete()