from ollama import embeddings


def generate_embedding(
    text: str
) -> list[float]:

    response = embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    return response["embedding"]