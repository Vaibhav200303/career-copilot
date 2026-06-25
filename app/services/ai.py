from ollama import chat
import json
from app.core.config import settings



def analyze_skill_gap(
    resume_text: str,
    job_description: str
) -> dict:

    prompt = f"""
    You are an expert technical recruiter.

    Compare the resume with the job description.

    Rules:

    1. Every skill mentioned in the job description must appear in exactly one category:
    - matched_skills
    - missing_skills

    2. Never leave missing_skills empty unless every required skill is present.

    3. Generate 3-5 actionable recommendations based on missing skills.

    Return ONLY valid JSON.


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
        model=settings.OLLAMA_CHAT_MODEL,
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