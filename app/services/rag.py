from ollama import chat
from app.models import ChatMessage
from app.core.config import settings
def build_rag_prompt(
    chunks:list[str],
    question:str,
    chat_history:list[ChatMessage] | None=None
)->str:
    context="\n\n".join(chunks)
    history=""
    if chat_history:
        history="\n".join(f"{message.role.title()}:{message.content}" for message in chat_history)
    return f"""
        You are Career Copilot, an AI career assistant.

        Use both the conversation history and the retrieved career knowledge to answer the user's question.

        If the answer exists in the retrieved context, prioritize it.

        If the answer is not available, clearly state that the information is unavailable instead of making assumptions.

        Conversation History:
        {history}

        Knowledge Base:
        {context}

        Current Question:
        {question}
    """


def generate_rag_response(
    prompt:str,

)->str:
    response=chat(
        model=settings.OLLAMA_CHAT_MODEL,
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