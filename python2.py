
# Traffic Violation Penalty Calculator

# Predefined fine rules (illustrative amounts in INR)
FINE_RULES = {
    "Car": {
        "Overspeeding": 1000,
        "No Helmet": 0,
        "Drunk Driving": 10000,
        "Signal Jumping": 1000
    },
    "Bike": {
        "Overspeeding": 1000,
        "No Helmet": 500,
        "Drunk Driving": 10000,
        "Signal Jumping": 1000
    },
    "Truck": {
        "Overspeeding": 2000,
        "No Helmet": 0,
        "Drunk Driving": 10000,
        "Signal Jumping": 2000
    }
}

# Repeat-offence rules
REPEAT_MULTIPLIER = 2

# Illustrative disqualification conditions
DISQUALIFICATION_OFFENCES = {
    "Drunk Driving"
}

def calculate_penalty(vehicle, offence, repeat):
    """Calculate the fine and disqualification status."""

    fine = FINE_RULES[vehicle][offence]

    if repeat:
        fine *= REPEAT_MULTIPLIER

    disqualified = offence in DISQUALIFICATION_OFFENCES

    return fine, disqualified


def main():
    violations = []
    total_penalty = 0
    disqualification_required = False

    print("TRAFFIC VIOLATION PENALTY CALCULATOR")
    print("-" * 45)

    vehicle_types = list(FINE_RULES.keys())

    print("Vehicle categories:", ", ".join(vehicle_types))

    for vehicle in vehicle_types:
        print(f"\n{vehicle} offence rules:")
        for offence, fine in FINE_RULES[vehicle].items():
            print(f"  {offence}: Rs. {fine}")

    count = int(input("\nEnter the number of violations: "))

    for i in range(1, count + 1):
        print(f"\nViolation {i}")

        vehicle = input("Enter vehicle category (Car/Bike/Truck): ").title()

        if vehicle not in FINE_RULES:
            print("Invalid vehicle category. Please try again.")
            continue

        print("Available offences:", ", ".join(FINE_RULES[vehicle]))
        offence = input("Enter offence type: ").strip().title()

        if offence not in FINE_RULES[vehicle]:
            print("Invalid offence type. Violation skipped.")
            continue

        repeat_input = input(
            "Is this a repeat offence? (yes/no): "
        ).strip().lower()

        if repeat_input not in ("yes", "no"):
            print("Invalid repeat-offence status. Violation skipped.")
            continue

        repeat = repeat_input == "yes"

        fine, disqualified = calculate_penalty(
            vehicle, offence, repeat
        )

        total_penalty += fine
        disqualification_required |= disqualified

        violations.append({
            "vehicle": vehicle,
            "offence": offence,
            "repeat": repeat,
            "fine": fine,
            "disqualified": disqualified
        })

    print("\n" + "=" * 55)
    print("             PENALTY REPORT")
    print("=" * 55)

    if not violations:
        print("No valid violations were recorded.")

    for i, violation in enumerate(violations, start=1):
        print(f"\nViolation {i}")
        print(f"Vehicle Category : {violation['vehicle']}")
        print(f"Offence Type     : {violation['offence']}")
        print(f"Repeat Offence   : {'Yes' if violation['repeat'] else 'No'}")
        print(f"Final Fine       : Rs. {violation['fine']}")
        print(
            "Disqualification: "
            + ("Required" if violation['disqualified'] else "Not triggered")
        )

    print("\nTotal Penalty: Rs.", total_penalty)

    if disqualification_required:
        print("Overall Status: Disqualification condition triggered.")
    else:
        print("Overall Status: No disqualification condition triggered.")

    print("=" * 55)


if __name__ == "__main__":
    main()
