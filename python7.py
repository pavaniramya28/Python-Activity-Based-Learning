PASS_MARK = 35
MIN_ATTENDANCE = 75.0


def read_positive_integer(message):
    """Read a positive integer."""
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Error: Enter a value greater than zero.")

        except ValueError:
            print("Error: Enter a valid integer.")


def read_percentage(message):
    """Read a percentage between 0 and 100."""
    while True:
        try:
            value = float(input(message))

            if 0 <= value <= 100:
                return value

            print("Error: Percentage must be between 0 and 100.")

        except ValueError:
            print("Error: Enter a valid numeric value.")


def read_marks(message):
    """Read marks between 0 and 100."""
    while True:
        try:
            value = float(input(message))

            if 0 <= value <= 100:
                return value

            print("Error: Marks must be between 0 and 100.")

        except ValueError:
            print("Error: Enter valid marks.")


def read_student_details():
    """Collect student identification details."""
    while True:
        name = input("Enter student name: ").strip()

        if name:
            break

        print("Error: Name cannot be empty.")

    while True:
        roll_number = input("Enter roll number: ").strip()

        if roll_number:
            break

        print("Error: Roll number cannot be empty.")

    return name, roll_number


def collect_subject_records(semester_count, subject_count):
    """Collect marks, attendance and prerequisite information."""
    subjects = []
    existing_names = set()

    for subject_index in range(subject_count):
        print(f"\nSUBJECT {subject_index + 1}")

        while True:
            subject_name = input("Enter subject name: ").strip()

            if not subject_name:
                print("Error: Subject name cannot be empty.")

            elif subject_name.casefold() in existing_names:
                print("Error: Subject already entered.")

            else:
                existing_names.add(subject_name.casefold())
                break

        semester_marks = []

        for semester in range(1, semester_count + 1):
            marks = read_marks(
                f"Enter marks for Semester {semester}: "
            )
            semester_marks.append(marks)

        attendance = read_percentage(
            "Enter attendance percentage: "
        )

        while True:
            prerequisite = input(
                "Are all prerequisites completed? (Y/N): "
            ).strip().upper()

            if prerequisite in ("Y", "N"):
                break

            print("Error: Enter Y or N.")

        subjects.append({
            "name": subject_name,
            "marks": semester_marks,
            "attendance": attendance,
            "prerequisite": prerequisite
        })

    return subjects


def audit_academic_progress(subjects):
    """Check all academic progression conditions."""
    failed_subjects = []
    attendance_shortages = []
    pending_prerequisites = []

    for subject in subjects:
        for semester, marks in enumerate(
            subject["marks"], start=1
        ):
            if marks < PASS_MARK:
                failed_subjects.append(
                    (subject["name"], semester, marks)
                )

        if subject["attendance"] < MIN_ATTENDANCE:
            attendance_shortages.append(
                (subject["name"], subject["attendance"])
            )

        if subject["prerequisite"] == "N":
            pending_prerequisites.append(subject["name"])

    eligible = not (
        failed_subjects
        or attendance_shortages
        or pending_prerequisites
    )

    return {
        "failed_subjects": failed_subjects,
        "attendance_shortages": attendance_shortages,
        "pending_prerequisites": pending_prerequisites,
        "eligible": eligible
    }


def display_report(name, roll_number, subjects, audit):
    """Display the academic progression report."""
    print("\n========== UNIVERSITY ACADEMIC PROGRESSION AUDIT ==========")
    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll_number}")

    print("\nSUBJECT-WISE ACADEMIC RECORD")

    for subject in subjects:
        print(f"\nSubject: {subject['name']}")
        print(f"Semester Marks: {subject['marks']}")
        print(f"Attendance: {subject['attendance']:.2f}%")
        print(
            f"Prerequisite Completed: "
            f"{subject['prerequisite']}"
        )

    print("\n========== OUTSTANDING REQUIREMENTS ==========")

    print("\nFailed Subjects:")
    if audit["failed_subjects"]:
        for subject, semester, marks in audit["failed_subjects"]:
            print(
                f"{subject} - Semester {semester}: "
                f"{marks:.2f} marks"
            )
    else:
        print("None")

    print("\nAttendance Shortages:")
    if audit["attendance_shortages"]:
        for subject, attendance in audit["attendance_shortages"]:
            print(
                f"{subject}: {attendance:.2f}% "
                f"(Required: {MIN_ATTENDANCE:.2f}%)"
            )
    else:
        print("None")

    print("\nPending Prerequisites:")
    if audit["pending_prerequisites"]:
        for subject in audit["pending_prerequisites"]:
            print(subject)
    else:
        print("None")

    print("\n========== FINAL PROGRESSION DECISION ==========")

    if audit["eligible"]:
        print("PROGRESSION STATUS: ELIGIBLE")
    else:
        print("PROGRESSION STATUS: NOT ELIGIBLE")


def main():
    print("UNIVERSITY ACADEMIC PROGRESSION AUDIT SYSTEM")

    name, roll_number = read_student_details()

    semester_count = read_positive_integer(
        "Enter number of semesters: "
    )

    subject_count = read_positive_integer(
        "Enter number of subjects: "
    )

    subjects = collect_subject_records(
        semester_count, subject_count
    )

    audit = audit_academic_progress(subjects)

    display_report(name, roll_number, subjects, audit)


if __name__ == "__main__":
    main()