from ollama import chat
import json

def analyze_skill_gap(
    resume_text: str,
    job_description: str
) -> str:
    prompt = f"""
    You are an AI career coach.

    Compare the resume and job description.

    Return ONLY valid JSON.

    Do not include markdown.
    Do not include explanations.
    Do not wrap the JSON in code blocks.

    Use this exact format:

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
                "role": "user",
                "content": prompt
            }
        ]
    )

    content= response["message"]["content"]
    return json.loads(content)