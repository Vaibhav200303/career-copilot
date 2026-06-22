from ollama import chat

def generate_learning_response(
        missing_skills:list[str]
)->str:
   
    prompt = f"""
    Create a 4-week learning roadmap for these skills:

    {", ".join(missing_skills)}

    For each week include:

    - Topics to learn
    - One project idea
    - Expected outcome
    """

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"] 