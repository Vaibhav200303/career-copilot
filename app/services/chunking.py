def chunk_text(
    text: str,
    chunk_size: int = 300,
    overlap:int =50,
) -> list[str]:

    words = text.split()

    chunks = []
    step=chunk_size-overlap
    for i in range(
        0,
        len(words),
        step
    ):
        chunk = words[i:i + chunk_size]
        chunks.append(
            " ".join(chunk)
        )

    return chunks