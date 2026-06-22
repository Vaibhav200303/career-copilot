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