from ollama import chat


def analyze_skill_gap(
    resume_text: str,
    job_description: str
) -> str:
    prompt = f"""
    You are an AI career coach.

    Compare the resume with the job description.

    Return your response in valid JSON with this exact structure:

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

    return response["message"]["content"]