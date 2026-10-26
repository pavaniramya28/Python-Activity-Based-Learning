
# University Academic Progression Audit System

# Predefined academic rules (illustrative)
PASS_MARK = 40
MIN_ATTENDANCE = 75
MIN_SEMESTER_AVERAGE = 50

# Subject prerequisites
PREREQUISITES = {
    "Advanced Python": ["Python Basics"],
    "Database Management": ["Computer Fundamentals"],
    "Web Development": ["HTML Basics", "CSS Basics"]
}


def audit_student(student):
    """Check marks, attendance, prerequisites and progression eligibility."""

    issues = []
    subject_results = {}

    marks = student["marks"]
    attendance = student["attendance"]
    completed = set(student["completed_subjects"])

    # Check each subject's pass condition
    for subject, score in marks.items():
        if not isinstance(score, (int, float)) or isinstance(score, bool) or not 0 <= score <= 100:
            issues.append(f"{subject}: Invalid marks.")
            subject_results[subject] = "Invalid"
        elif score < PASS_MARK:
            issues.append(f"{subject}: Failed (marks: {score}).")
            subject_results[subject] = "Fail"
        else:
            subject_results[subject] = "Pass"

    # Calculate semester average only if all marks are valid
    valid_marks = all(
        isinstance(score, (int, float))
        and not isinstance(score, bool)
        and 0 <= score <= 100
        for score in marks.values()
    )

    average = (
        sum(marks.values()) / len(marks)
        if marks and valid_marks else None
    )

    if average is None:
        issues.append("Semester average cannot be calculated.")
    elif average < MIN_SEMESTER_AVERAGE:
        issues.append(
            f"Semester average below {MIN_SEMESTER_AVERAGE}%."
        )

    # Check attendance
    if not isinstance(student["attendance"], (int, float)) or isinstance(student["attendance"], bool) or not 0 <= attendance <= 100:
        issues.append("Invalid attendance percentage.")
    elif attendance < MIN_ATTENDANCE:
        issues.append(
            f"Attendance below required {MIN_ATTENDANCE}%."
        )

    # Check prerequisite completion
    for subject, prerequisites in PREREQUISITES.items():
        if subject in marks:
            for prerequisite in prerequisites:
                if prerequisite not in completed:
                    issues.append(
                        f"{subject}: Prerequisite '{prerequisite}' "
                        "is not completed."
                    )

    eligible = len(issues) == 0

    return {
        "subject_results": subject_results,
        "average": average,
        "issues": issues,
        "eligible": eligible
    }


def display_report(student, result):
    """Display the academic progression audit report."""

    print("\nUNIVERSITY ACADEMIC PROGRESSION AUDIT")
    print("=" * 55)
    print(f"Student ID: {student['student_id']}")
    print(f"Student Name: {student['name']}")

    print("\nSUBJECT RESULTS")
    print("-" * 35)

    for subject, status in result["subject_results"].items():
        print(f"{subject:<25} {status}")

    print("\nACADEMIC SUMMARY")
    print("-" * 35)

    if result["average"] is None:
        print("Semester Average: Not available")
    else:
        print(f"Semester Average: {result['average']:.2f}%")

    print(f"Attendance: {student['attendance']}%")

    print("\nOUTSTANDING REQUIREMENTS")
    print("-" * 35)

    if result["issues"]:
        for number, issue in enumerate(result["issues"], start=1):
            print(f"{number}. {issue}")
    else:
        print("No outstanding requirements.")

    print("\nPROGRESSION DECISION")
    print("-" * 35)

    if result["eligible"]:
        print("Status: ELIGIBLE FOR PROGRESSION")
    else:
        print("Status: NOT ELIGIBLE FOR PROGRESSION")


def main():
    # Hypothetical student academic record
    student = {
        "student_id": "STU101",
        "name": "Rahul",
        "marks": {
            "Python": 75,
            "Mathematics": 35,
            "Database Management": 68,
            "Web Development": 80
        },
        "attendance": 82,
        "completed_subjects": [
            "Python Basics",
            "Computer Fundamentals",
            "HTML Basics"
        ]
    }

    result = audit_student(student)
    display_report(student, result)


if __name__ == "__main__":
    main()
