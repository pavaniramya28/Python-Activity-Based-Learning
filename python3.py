
# Laboratory Chemical Inventory Validation System

# Illustrative inventory rules for an academic assignment.
# Replace these values with the rules supplied in the question.

STORAGE_RULES = {
    "General": {
        "max_quantity": 100,
        "incompatible": {"Oxidizer", "Flammable", "Corrosive"}
    },
    "Flammable": {
        "max_quantity": 50,
        "incompatible": {"Oxidizer", "Corrosive"}
    },
    "Oxidizer": {
        "max_quantity": 30,
        "incompatible": {"Flammable", "Organic"}
    },
    "Corrosive": {
        "max_quantity": 40,
        "incompatible": {"Flammable", "Oxidizer"}
    },
    "Organic": {
        "max_quantity": 60,
        "incompatible": {"Oxidizer"}
    }
}


def validate_inventory(chemicals):
    """Validate quantity limits, storage categories and compatibility."""

    errors = []

    # Check individual records
    for chemical in chemicals:
        name = chemical["name"]
        category = chemical["category"]
        quantity = chemical["quantity"]

        if category not in STORAGE_RULES:
            errors.append(
                f"{name}: Invalid storage category '{category}'."
            )
            continue

        max_quantity = STORAGE_RULES[category]["max_quantity"]

        if quantity <= 0:
            errors.append(
                f"{name}: Quantity must be greater than zero."
            )
        elif quantity > max_quantity:
            errors.append(
                f"{name}: Quantity {quantity} exceeds "
                f"the limit of {max_quantity}."
            )

    # Check compatibility between chemicals sharing a storage area
    for i in range(len(chemicals)):
        first = chemicals[i]

        if first["category"] not in STORAGE_RULES:
            continue

        for j in range(i + 1, len(chemicals)):
            second = chemicals[j]

            if second["category"] not in STORAGE_RULES:
                continue

            if first["storage_area"] != second["storage_area"]:
                continue

            first_category = first["category"]
            second_category = second["category"]

            incompatible = (
                second_category
                in STORAGE_RULES[first_category]["incompatible"]
            )

            if incompatible:
                errors.append(
                    f"Compatibility violation: {first['name']} "
                    f"({first_category}) and {second['name']} "
                    f"({second_category}) share storage area "
                    f"'{first['storage_area']}'."
                )

    return errors


def display_report(chemicals, errors):
    """Display inventory records and validation results."""

    print("\nLABORATORY CHEMICAL INVENTORY REPORT")
    print("=" * 55)

    for chemical in chemicals:
        print(
            f"Name: {chemical['name']} | "
            f"Category: {chemical['category']} | "
            f"Quantity: {chemical['quantity']} | "
            f"Area: {chemical['storage_area']}"
        )

    print("\nVALIDATION RESULTS")
    print("-" * 55)

    if errors:
        for number, error in enumerate(errors, start=1):
            print(f"{number}. {error}")

        print(f"\nTotal issues found: {len(errors)}")
        print("Inventory Status: INVALID")
    else:
        print("No validation issues found.")
        print("Inventory Status: VALID")


def main():
    # Hypothetical inventory records
    chemicals = [
        {
            "name": "Ethanol",
            "category": "Flammable",
            "quantity": 60,
            "storage_area": "Cabinet-A"
        },
        {
            "name": "Hydrogen Peroxide",
            "category": "Oxidizer",
            "quantity": 20,
            "storage_area": "Cabinet-A"
        },
        {
            "name": "Acetic Acid",
            "category": "Corrosive",
            "quantity": 25,
            "storage_area": "Cabinet-B"
        },
        {
            "name": "Organic Solvent",
            "category": "Organic",
            "quantity": 15,
            "storage_area": "Cabinet-C"
        }
    ]

    errors = validate_inventory(chemicals)
    display_report(chemicals, errors)


if __name__ == "__main__":
    main()
