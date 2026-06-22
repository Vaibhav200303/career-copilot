import json

from ollama import chat

from app.schemas import RoadmapResponse


def generate_learning_roadmap(
    missing_skills: list[str]
) -> RoadmapResponse:

    prompt = f"""
    You are an experienced career mentor.

    Create a practical 4-week learning roadmap for these skills:

    {", ".join(missing_skills)}

    Return ONLY valid JSON.

    Do not include markdown.
    Do not include explanations.
    Do not wrap the response in code blocks.

    Use this exact schema:

    {{
      "weeks": [
        {{
          "week": 1,
          "topics": [],
          "project": "",
          "outcome": ""
        }}
      ]
    }}
    """

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": "You are a career mentor. Always respond with valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    roadmap = json.loads(
        response["message"]["content"]
    )

    return RoadmapResponse(**roadmap)