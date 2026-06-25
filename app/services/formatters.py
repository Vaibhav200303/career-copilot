def format_analysis_for_ingestion(
    matched_skills: list[str],
    missing_skills: list[str],
    recommendations: list[str],
) -> str:

    sections = [
        "Matched Skills:",
        "\n".join(matched_skills),
        "",
        "Missing Skills:",
        "\n".join(missing_skills),
        "",
        "Recommendations:",
        "\n".join(recommendations),
    ]

    return "\n".join(sections)



def format_roadmap_for_ingestion(
    roadmap_content: dict,
) -> str:

    sections = []

    for week in roadmap_content["weeks"]:

        sections.append(
            f"Week {week['week']}"
        )

        sections.append("Topics:")
        sections.append(
            "\n".join(
                week["topics"]
            )
        )

        sections.append(
            f"Project:\n{week['project']}"
        )

        sections.append(
            f"Outcome:\n{week['outcome']}"
        )

        sections.append("")

    return "\n".join(sections)



def format_interview_experience_for_ingestion(
    company: str,
    role: str,
    interview_type: str,
    outcome: str,
    questions_asked: list[str],
    experience: str,
    lessons_learned: str,
) -> str:

    sections = [
        f"Company: {company}",
        f"Role: {role}",
        f"Interview Type: {interview_type}",
        f"Outcome: {outcome}",
        "",
        "Questions Asked:",
        "\n".join(questions_asked),
        "",
        "Experience:",
        experience,
        "",
        "Lessons Learned:",
        lessons_learned,
    ]

    return "\n".join(sections)