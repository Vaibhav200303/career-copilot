from ollama import chat
def build_rag_prompt(
    chunks:list[str],
    question:str
)->str:
    context="\n\n".join(chunks)
    return f"""
        You are Career Copilot, an AI career assistant.

        Use the provided context to answer the user's question.

        If the answer exists in the context, use it.

        If the answer is not available in the context, clearly say that the information is not available.

        Context:
        {context}

        Question:
        {question}
    """


def generate_rag_response(
    prompt:str,

)->str:
    response=chat(
        model="qwen3:8b",
        messages=[
            {
                "role":"system",
                "content":(
                    "You are Career Copilot."
                    "Provide clear and actionable career advice."
                ),
            },
            {
                "role":"user",
                "content":prompt
            },
        ],
    )
    return response["message"]["content"]