
"""
Case Study 12: Attendance Recovery Computation

Description:
Calculates current attendance and determines the minimum
consecutive classes required to achieve the eligibility
threshold under different future absence scenarios.
"""

import math

# Academic attendance policy
ELIGIBILITY_THRESHOLD = 75.0


def calculate_percentage(attended, conducted):
    """Calculate attendance percentage."""
    return (attended / conducted) * 100


def calculate_recovery(attended, conducted, absences):
    """
    Calculate the minimum consecutive classes required
    after a specified number of future absences.
    """

    updated_attended = attended
    updated_conducted = conducted + absences

    numerator = (
        ELIGIBILITY_THRESHOLD * updated_conducted
        - 100 * updated_attended
    )

    denominator = 100 - ELIGIBILITY_THRESHOLD

    required_classes = max(
        0,
        math.ceil(numerator / denominator)
    )

    final_attended = updated_attended + required_classes
    final_conducted = updated_conducted + required_classes

    projected_percentage = calculate_percentage(
        final_attended, final_conducted
    )

    return required_classes, projected_percentage


def validate_attendance(conducted, attended):
    """Validate attendance input values."""
    if conducted <= 0:
        return False

    if attended < 0 or attended > conducted:
        return False

    return True


def read_integer(prompt):
    """Read a valid integer from the user."""
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Please enter a non-negative value.")
                continue

            return value

        except ValueError:
            print("Invalid input. Enter a whole number.")


def display_report(name, attended, conducted, scenarios):
    """Display current attendance and recovery scenarios."""

    current_percentage = calculate_percentage(
        attended, conducted
    )

    print("\n" + "=" * 68)
    print("             ATTENDANCE RECOVERY REPORT")
    print("=" * 68)

    print(f"Student Name          : {name}")
    print(f"Classes Conducted     : {conducted}")
    print(f"Classes Attended      : {attended}")
    print(f"Current Attendance    : {current_percentage:.2f}%")
    print(f"Eligibility Threshold : {ELIGIBILITY_THRESHOLD:.2f}%")

    if current_percentage >= ELIGIBILITY_THRESHOLD:
        print("Current Status        : ELIGIBLE")
    else:
        print("Current Status        : NOT ELIGIBLE")

    print("-" * 68)
    print("             FUTURE ATTENDANCE SCENARIOS")
    print("-" * 68)

    print(
        f"{'Absences':<15}{'Required Classes':<20}"
        f"{'Projected Attendance':<25}"
    )

    print("-" * 68)

    for absences in scenarios:
        required, projected = calculate_recovery(
            attended, conducted, absences
        )

        print(
            f"{absences:<15}{required:<20}"
            f"{projected:.2f}%"
        )

    print("-" * 68)
    print("Note: All recovery classes must be attended consecutively.")
    print("=" * 68)


def main():
    """Main function to execute attendance processing."""

    print("=" * 55)
    print("       ATTENDANCE RECOVERY COMPUTATION SYSTEM")
    print("=" * 55)

    student_name = input("Enter student name: ").strip()

    while not student_name:
        print("Student name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    total_classes = read_integer(
        "Enter total classes conducted: "
    )

    while total_classes == 0:
        print("Total classes must be greater than zero.")
        total_classes = read_integer(
            "Enter total classes conducted: "
        )

    attended_classes = read_integer(
        "Enter classes attended: "
    )

    while not validate_attendance(
        total_classes, attended_classes
    ):
        print("Invalid attendance details.")
        attended_classes = read_integer(
            "Re-enter classes attended: "
        )

    scenario_count = read_integer(
        "Enter number of future scenarios: "
    )

    while scenario_count == 0:
        print("Enter at least one scenario.")
        scenario_count = read_integer(
            "Enter number of future scenarios: "
        )

    scenarios = []

    for index in range(scenario_count):
        print(f"\nScenario {index + 1}")

        future_absences = read_integer(
            "Enter possible future absences: "
        )

        scenarios.append(future_absences)

    display_report(
        student_name,
        attended_classes,
        total_classes,
        scenarios
    )


if __name__ == "__main__":
    main()
