from ollama import embeddings
from app.core.config import settings


def generate_embedding(
    text: str
) -> list[float]:

    response = embeddings(
        model=settings.OLLAMA_EMBEDDING_MODEL,
        prompt=text
    )

    return response["embedding"]