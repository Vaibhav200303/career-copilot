from ollama import chat
import json


def analyze_skill_gap(
    resume_text: str,
    job_description: str
) -> dict:

    prompt = f"""
    Compare the resume and job description.

    Return ONLY valid JSON using this exact schema:

    {{
      "matched_skills": [],
      "missing_skills": [],
      "recommendations": []
    }}

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": "You are an AI career coach. Respond only with valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    return json.loads(response["message"]["content"])