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


def read_non_negative_integer(message):
    """Read a non-negative integer."""
    while True:
        try:
            value = int(input(message))

            if value >= 0:
                return value

            print("Error: Value cannot be negative.")

        except ValueError:
            print("Error: Enter a valid integer.")


def read_positive_number(message):
    """Read a positive price."""
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Error: Price must be greater than zero.")

        except ValueError:
            print("Error: Enter a valid numeric value.")


def read_discount():
    """Read a discount percentage from 0 to 100."""
    while True:
        try:
            value = float(input("Enter discount percentage: "))

            if 0 <= value <= 100:
                return value

            print("Error: Discount must be between 0 and 100.")

        except ValueError:
            print("Error: Enter a valid percentage.")


def read_product_name(existing_names):
    """Read a unique product name."""
    while True:
        name = input("Enter product name: ").strip()

        if not name:
            print("Error: Product name cannot be empty.")

        elif name.casefold() in existing_names:
            print("Error: Product name already exists.")

        else:
            return name


def process_product(existing_names):
    """Process one product order and stock reconciliation."""
    name = read_product_name(existing_names)

    opening_stock = read_non_negative_integer(
        "Enter opening stock: "
    )

    unit_price = read_positive_number(
        "Enter unit price: "
    )

    ordered_quantity = read_positive_integer(
        "Enter ordered quantity: "
    )

    discount = read_discount()

    while True:
        dispatched = read_non_negative_integer(
            "Enter dispatched quantity: "
        )

        if dispatched <= ordered_quantity and dispatched <= opening_stock:
            break

        print(
            "Error: Dispatch cannot exceed ordered quantity "
            "or available stock."
        )

    while True:
        returned = read_non_negative_integer(
            "Enter returned quantity: "
        )

        if returned <= dispatched:
            break

        print("Error: Returns cannot exceed dispatched quantity.")

    net_sold = dispatched - returned

    discounted_price = unit_price * (1 - discount / 100)

    revenue = net_sold * discounted_price

    expected_closing = opening_stock - dispatched + returned

    physical_closing = read_non_negative_integer(
        "Enter physical closing stock: "
    )

    discrepancy = physical_closing - expected_closing

    if discrepancy < 0:
        status = "SHORTAGE"
    elif discrepancy > 0:
        status = "EXCESS"
    else:
        status = "MATCHED"

    return {
        "name": name,
        "opening": opening_stock,
        "ordered": ordered_quantity,
        "dispatched": dispatched,
        "returned": returned,
        "net_sold": net_sold,
        "unit_price": unit_price,
        "discount": discount,
        "revenue": revenue,
        "expected": expected_closing,
        "physical": physical_closing,
        "discrepancy": discrepancy,
        "status": status
    }


def generate_summary(records):
    """Calculate overall revenue and inventory totals."""
    total_revenue = sum(item["revenue"] for item in records)

    total_expected = sum(item["expected"] for item in records)

    total_physical = sum(item["physical"] for item in records)

    total_discrepancy = total_physical - total_expected

    return {
        "revenue": total_revenue,
        "expected_stock": total_expected,
        "physical_stock": total_physical,
        "discrepancy": total_discrepancy
    }


def display_report(records, summary):
    """Display order processing and reconciliation results."""
    print("\n========== E-COMMERCE ORDER REPORT ==========")

    for item in records:
        print(f"\nProduct: {item['name']}")
        print(f"Opening Stock: {item['opening']}")
        print(f"Ordered Quantity: {item['ordered']}")
        print(f"Dispatched Quantity: {item['dispatched']}")
        print(f"Returned Quantity: {item['returned']}")
        print(f"Net Sold Quantity: {item['net_sold']}")
        print(f"Discount: {item['discount']:.2f}%")
        print(f"Revenue: Rs. {item['revenue']:.2f}")
        print(f"Expected Closing Stock: {item['expected']}")
        print(f"Physical Closing Stock: {item['physical']}")
        print(f"Stock Discrepancy: {item['discrepancy']}")
        print(f"Stock Status: {item['status']}")

    print("\n========== FINAL INVENTORY SUMMARY ==========")

    print(f"Total Revenue: Rs. {summary['revenue']:.2f}")
    print(f"Expected Closing Stock: {summary['expected_stock']}")
    print(f"Physical Closing Stock: {summary['physical_stock']}")
    print(f"Overall Stock Discrepancy: {summary['discrepancy']}")

    matched = sum(
        item["status"] == "MATCHED" for item in records
    )

    shortages = sum(
        item["status"] == "SHORTAGE" for item in records
    )

    excesses = sum(
        item["status"] == "EXCESS" for item in records
    )

    print(f"Matched Products: {matched}")
    print(f"Products with Shortage: {shortages}")
    print(f"Products with Excess: {excesses}")


def main():
    print("INTEGRATED E-COMMERCE ORDER PROCESSING SYSTEM")

    product_count = read_positive_integer(
        "Enter number of products: "
    )

    records = []
    existing_names = set()

    for index in range(product_count):
        print(f"\n========== PRODUCT {index + 1} ==========")

        record = process_product(existing_names)

        existing_names.add(record["name"].casefold())
        records.append(record)

    summary = generate_summary(records)

    display_report(records, summary)


if __name__ == "__main__":
    main()