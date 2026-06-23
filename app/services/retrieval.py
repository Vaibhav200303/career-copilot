from sqlalchemy.orm import Session
from app.models import Document
from app.services.document_ingestion import generate_embedding

def retrieve_relevant_chunks(
    db:Session,
    user_id:int,
    query:str,
    top_k:int=5
)->list[str]:
    query_embedding=generate_embedding(query)
    documents = (
        db.query(Document)
        .filter(
            Document.user_id == user_id
        )
        .order_by(
            Document.embedding.cosine_distance(
                query_embedding
            )
        )
        .limit(top_k)
        .all()
    )
    return [document.content for document in documents]