
"""
Case Study: Examination Result and Grace-Mark Validation
Description: Calculates examination results, applies grace marks,
             validates subject-wise passing criteria, and assigns
             final classifications.
"""

# Academic rules
SUBJECTS = ["Python", "Mathematics", "Physics", "Chemistry", "English"]
MAX_MARKS = 100
PASS_MARKS = 35
TOTAL_GRACE_LIMIT = 5


def read_marks(subject):
    """Read and validate marks for a subject."""
    while True:
        try:
            marks = int(input(f"Enter marks in {subject} (0-100): "))

            if 0 <= marks <= MAX_MARKS:
                return marks

            print("Invalid input. Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def apply_grace_marks(marks):
    """Apply eligible grace marks within the total allowance."""
    adjusted_marks = marks.copy()
    grace_awarded = [0] * len(marks)
    remaining_grace = TOTAL_GRACE_LIMIT

    for index, mark in enumerate(marks):
        if mark < PASS_MARKS:
            shortfall = PASS_MARKS - mark

            if shortfall <= remaining_grace:
                grace_awarded[index] = shortfall
                adjusted_marks[index] += shortfall
                remaining_grace -= shortfall

    return adjusted_marks, grace_awarded


def get_classification(percentage, all_subjects_passed):
    """Determine the final result and classification."""
    if not all_subjects_passed:
        return "FAIL", "Not Classified"

    if percentage >= 75:
        return "PASS", "Distinction"
    elif percentage >= 60:
        return "PASS", "First Class"
    elif percentage >= 50:
        return "PASS", "Second Class"
    else:
        return "PASS", "Pass Class"


def display_report(name, original, adjusted, grace):
    """Display the final examination report."""
    maximum_total = len(SUBJECTS) * MAX_MARKS
    initial_total = sum(original)
    final_total = sum(adjusted)
    percentage = (final_total / maximum_total) * 100

    all_subjects_passed = all(
        mark >= PASS_MARKS for mark in adjusted
    )

    result, classification = get_classification(
        percentage, all_subjects_passed
    )

    print("\n" + "=" * 65)
    print("             EXAMINATION RESULT REPORT")
    print("=" * 65)
    print(f"Student Name       : {name}")
    print("-" * 65)
    print(f"{'Subject':<18}{'Original':>10}{'Grace':>10}"
          f"{'Final':>10}{'Status':>12}")
    print("-" * 65)

    for subject, old, bonus, final in zip(
        SUBJECTS, original, grace, adjusted
    ):
        status = "PASS" if final >= PASS_MARKS else "FAIL"

        print(
            f"{subject:<18}{old:>10}{bonus:>10}"
            f"{final:>10}{status:>12}"
        )

    print("-" * 65)
    print(f"Initial Total      : {initial_total}/{maximum_total}")
    print(f"Final Total        : {final_total}/{maximum_total}")
    print(f"Percentage         : {percentage:.2f}%")
    print(f"Grace Marks Used   : {sum(grace)}/{TOTAL_GRACE_LIMIT}")
    print(f"Overall Result     : {result}")
    print(f"Classification     : {classification}")
    print("=" * 65)


def main():
    """Control the examination result processing."""
    print("=" * 50)
    print(" EXAMINATION RESULT AND GRACE-MARK VALIDATION")
    print("=" * 50)

    student_name = input("Enter student name: ").strip()

    while not student_name:
        print("Student name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    original_marks = [
        read_marks(subject) for subject in SUBJECTS
    ]

    adjusted_marks, grace_marks = apply_grace_marks(
        original_marks
    )

    display_report(
        student_name,
        original_marks,
        adjusted_marks,
        grace_marks
    )


if __name__ == "__main__":
    main()
