import json

from ollama import chat

from app.schemas import InterviewResponse


def generate_interview_questions(
    matched_skills: list[str],
    missing_skills: list[str]
) -> InterviewResponse:

    prompt = f"""
    Generate 10 interview questions.

    Matched skills:
    {", ".join(matched_skills)}

    Missing skills:
    {", ".join(missing_skills)}

    Return ONLY valid JSON.

    Use this schema:

    {{
      "questions": [
        {{
          "question": "",
          "category": "",
          "difficulty": ""
        }}
      ]
    }}
    """

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": "You are an expert technical interviewer. Return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    data = json.loads(
        response["message"]["content"]
    )

    return InterviewResponse(**data)