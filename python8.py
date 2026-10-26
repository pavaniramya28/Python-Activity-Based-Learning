
# Smart Campus Incident and Maintenance Prioritization System

# Predefined severity scores
SEVERITY_SCORES = {
    "Critical": 5,
    "High": 4,
    "Medium": 3,
    "Low": 2
}

# Location importance scores
LOCATION_SCORES = {
    "Laboratory": 5,
    "Library": 4,
    "Classroom": 3,
    "Cafeteria": 2,
    "Garden": 1
}

# Priority thresholds
CRITICAL_THRESHOLD = 80
HIGH_THRESHOLD = 60
MEDIUM_THRESHOLD = 35


def calculate_priority(incident):
    """Calculate priority using severity, location and frequency."""

    severity = SEVERITY_SCORES.get(incident["severity"], 0)
    location = LOCATION_SCORES.get(incident["location"], 0)
    frequency = incident["frequency"]

    # Frequency is capped to prevent excessive weighting
    frequency_score = min(frequency, 10)

    # Weighted priority score out of 100
    score = (
        severity * 10
        + location * 5
        + frequency_score * 2
    )

    # Classify incident based on score
    if incident["severity"] == "Critical" or score >= CRITICAL_THRESHOLD:
        priority = "Critical"
    elif score >= HIGH_THRESHOLD:
        priority = "High"
    elif score >= MEDIUM_THRESHOLD:
        priority = "Medium"
    else:
        priority = "Low"

    return score, priority


def validate_incident(incident):
    """Check whether an incident record is valid."""

    if incident["severity"] not in SEVERITY_SCORES:
        return "Invalid severity level."

    if incident["location"] not in LOCATION_SCORES:
        return "Invalid campus location."

    if (
        not isinstance(incident["frequency"], int)
        or isinstance(incident["frequency"], bool)
        or incident["frequency"] < 1
    ):
        return "Frequency must be a positive integer."

    return None


def prioritize_incidents(incidents):
    """Validate, rank and summarize maintenance incidents."""

    valid_incidents = []
    errors = []

    for incident in incidents:
        error = validate_incident(incident)

        if error:
            errors.append(
                f"{incident.get('id', 'Unknown')}: {error}"
            )
            continue

        score, priority = calculate_priority(incident)

        valid_incidents.append({
            **incident,
            "score": score,
            "priority": priority
        })

    # Rank by score, with higher scores first
    priority_order = {
        "Critical": 4,
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    valid_incidents.sort(
        key=lambda item: (
            priority_order[item["priority"]],
            item["score"]
        ),
        reverse=True
    )

    return valid_incidents, errors


def display_report(incidents, errors):
    """Display ranked incidents and priority summary."""

    print("\nSMART CAMPUS MAINTENANCE REPORT")
    print("=" * 75)

    for rank, incident in enumerate(incidents, start=1):
        print(f"\nRank: {rank}")
        print(f"Incident ID : {incident['id']}")
        print(f"Description : {incident['description']}")
        print(f"Severity    : {incident['severity']}")
        print(f"Location    : {incident['location']}")
        print(f"Frequency   : {incident['frequency']} reports")
        print(f"Score       : {incident['score']}/100")
        print(f"Priority    : {incident['priority']}")

    print("\nPRIORITY SUMMARY")
    print("-" * 40)

    for priority in ["Critical", "High", "Medium", "Low"]:
        count = sum(
            1 for item in incidents
            if item["priority"] == priority
        )
        print(f"{priority:<10}: {count}")

    if incidents:
        print(
            "\nHighest-priority case:",
            incidents[0]["id"],
            "-", incidents[0]["description"]
        )

    if errors:
        print("\nINVALID REPORTS")
        for error in errors:
            print("-", error)


def main():
    # Hypothetical campus maintenance reports
    reports = [
        {
            "id": "INC101",
            "description": "Electrical fault in laboratory",
            "severity": "Critical",
            "location": "Laboratory",
            "frequency": 3
        },
        {
            "id": "INC102",
            "description": "Broken lights in classroom",
            "severity": "Medium",
            "location": "Classroom",
            "frequency": 5
        },
        {
            "id": "INC103",
            "description": "Water leakage in library",
            "severity": "High",
            "location": "Library",
            "frequency": 7
        },
        {
            "id": "INC104",
            "description": "Damaged garden bench",
            "severity": "Low",
            "location": "Garden",
            "frequency": 2
        }
    ]

    ranked, errors = prioritize_incidents(reports)
    display_report(ranked, errors)


if __name__ == "__main__":
    main()
