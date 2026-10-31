from collections import defaultdict


def read_positive_integer(message):
    """Read and validate a positive integer."""
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Error: Enter a value greater than zero.")

        except ValueError:
            print("Error: Enter a valid integer.")


def read_roll_number(row, column):
    """Read a roll number or a special seat value."""
    while True:
        try:
            return int(
                input(f"Enter roll number at ({row}, {column}): ")
            )

        except ValueError:
            print("Error: Enter an integer value.")


def read_reserved_positions(rows, columns):
    """Collect valid reserved seat positions."""
    reserved = set()

    count = read_positive_integer(
        "Enter the number of reserved seats: "
    )

    for index in range(count):
        print(f"\nReserved seat {index + 1}")

        while True:
            row = read_positive_integer("Enter row number: ")
            column = read_positive_integer("Enter column number: ")

            if row > rows or column > columns:
                print("Error: Position is outside the seating matrix.")
            else:
                reserved.add((row, column))
                break

    return reserved


def create_seating_matrix(rows, columns):
    """Create and populate the seating matrix."""
    seating = []

    print("\nEnter roll numbers (0 = empty, negative = invalid).")

    for row in range(1, rows + 1):
        current_row = []

        for column in range(1, columns + 1):
            roll_number = read_roll_number(row, column)
            current_row.append(roll_number)

        seating.append(current_row)

    return seating


def validate_seating(seating, reserved):
    """Validate all student allocations."""
    positions = defaultdict(list)

    empty_seats = []
    invalid_allocations = []
    reserved_violations = []

    for row_index, row in enumerate(seating, start=1):
        for column_index, roll_number in enumerate(row, start=1):

            position = (row_index, column_index)

            if roll_number < 0:
                invalid_allocations.append(position)

            elif roll_number == 0:
                if position not in reserved:
                    empty_seats.append(position)

            else:
                positions[roll_number].append(position)

                if position in reserved:
                    reserved_violations.append(
                        (roll_number, position)
                    )

    duplicates = {
        roll_number: locations
        for roll_number, locations in positions.items()
        if len(locations) > 1
    }

    return (
        duplicates,
        empty_seats,
        invalid_allocations,
        reserved_violations
    )


def display_report(seating, reserved, results):
    """Display the seating matrix and validation report."""
    duplicates, empty, invalid, violations = results

    print("\n========== SEATING MATRIX ==========")

    for row in seating:
        print(" ".join(f"{value:>6}" for value in row))

    print("\n========== VALIDATION REPORT ==========")

    print(f"Reserved positions: {sorted(reserved)}")

    print("\nDuplicate Roll Numbers:")
    if duplicates:
        for roll_number, positions in duplicates.items():
            print(f"Roll No. {roll_number}: {positions}")
    else:
        print("None")

    print("\nOccupied Reserved Seats:")
    if violations:
        for roll_number, position in violations:
            print(f"Roll No. {roll_number} at {position}")
    else:
        print("None")

    print(f"\nEmpty Seats (excluding reserved): {empty}")
    print(f"Invalid Allocations: {invalid}")

    issue_count = (
        len(duplicates)
        + len(violations)
        + len(empty)
        + len(invalid)
    )

    print("\nOverall Status:")
    if issue_count == 0:
        print("VALID SEATING ARRANGEMENT")
    else:
        print("SEATING ARRANGEMENT REQUIRES CORRECTION")


def main():
    print("EXAMINATION SEATING VALIDATION SYSTEM")

    rows = read_positive_integer("Enter number of rows: ")
    columns = read_positive_integer("Enter number of columns: ")

    reserved = read_reserved_positions(rows, columns)

    seating = create_seating_matrix(rows, columns)

    results = validate_seating(seating, reserved)

    display_report(seating, reserved, results)


if __name__ == "__main__":
    main()