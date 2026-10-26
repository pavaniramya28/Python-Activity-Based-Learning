
# Nested List Examination Seating Validation System

# Configuration
ROWS = 3
COLS = 4

# Seat values: roll numbers are positive integers.
# 0 represents an empty seat.
# -1 represents a reserved seat.
RESERVED_POSITIONS = {(0, 2), (2, 3)}

# Hypothetical registered student roll numbers
VALID_ROLL_NUMBERS = {
    101, 102, 103, 104, 105, 106,
    107, 108, 109, 110
}


def validate_seating(matrix):
    """Validate the complete examination seating matrix."""
    errors = []
    roll_positions = {}

    # Check matrix dimensions
    if len(matrix) != ROWS:
        return ["Invalid number of rows in the seating matrix."]

    for row in matrix:
        if not isinstance(row, list) or len(row) != COLS:
            return ["Invalid seating matrix structure."]

    # Validate each seat
    for i in range(ROWS):
        for j in range(COLS):
            seat = matrix[i][j]
            position = (i, j)

            # Check reserved positions
            if position in RESERVED_POSITIONS:
                if seat != -1:
                    errors.append(
                        f"Seat ({i + 1}, {j + 1}) must be reserved."
                    )
                continue

            # Reserved marker in an ordinary seat
            if seat == -1:
                errors.append(
                    f"Seat ({i + 1}, {j + 1}) is not a reserved position."
                )
                continue

            # Check empty seats
            if seat == 0:
                errors.append(
                    f"Seat ({i + 1}, {j + 1}) is empty."
                )
                continue

            # Check roll number format
            if not isinstance(seat, int) or isinstance(seat, bool):
                errors.append(
                    f"Seat ({i + 1}, {j + 1}) has an invalid roll number."
                )
                continue

            # Check registered student allocation
            if seat not in VALID_ROLL_NUMBERS:
                errors.append(
                    f"Roll number {seat} at seat ({i + 1}, {j + 1}) "
                    "is not registered."
                )
                continue

            # Track roll number positions for duplicate detection
            if seat in roll_positions:
                errors.append(
                    f"Duplicate roll number {seat} at seats "
                    f"{roll_positions[seat]} and ({i + 1}, {j + 1})."
                )
            else:
                roll_positions[seat] = (i + 1, j + 1)

    return errors


def display_matrix(matrix):
    """Display the seating arrangement."""
    print("\nEXAMINATION SEATING MATRIX")
    print("-" * 35)

    for row in matrix:
        print(" ".join(f"{seat:>5}" for seat in row))

    print("\nLegend: -1 = Reserved, 0 = Empty")


def main():
    # Nested list representing the seating arrangement
    seating_matrix = [
        [101, 102, -1, 104],
        [105, 106, 105, 108],
        [109, 110, 111, -1]
    ]

    display_matrix(seating_matrix)

    errors = validate_seating(seating_matrix)

    print("\nVALIDATION REPORT")
    print("-" * 35)

    if errors:
        for number, error in enumerate(errors, start=1):
            print(f"{number}. {error}")

        print("\nFinal Status: INVALID SEATING ARRANGEMENT")
    else:
        print("All seating rules are satisfied.")
        print("\nFinal Status: VALID SEATING ARRANGEMENT")


if __name__ == "__main__":
    main()
