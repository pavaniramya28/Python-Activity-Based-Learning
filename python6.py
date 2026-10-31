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


def read_positive_number(message):
    """Read a positive product price."""
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Error: Price must be greater than zero.")

        except ValueError:
            print("Error: Enter a valid numeric value.")


def read_threshold():
    """Read a non-negative fluctuation threshold."""
    while True:
        try:
            value = float(
                input("Enter fluctuation threshold (%): ")
            )

            if value >= 0:
                return value

            print("Error: Threshold cannot be negative.")

        except ValueError:
            print("Error: Enter a valid numeric value.")


def collect_product_data(product_count, period_count):
    """Collect unique product names and historical prices."""
    product_names = []
    price_history = []

    for index in range(product_count):
        print(f"\nPRODUCT {index + 1}")

        while True:
            name = input("Enter product name: ").strip()

            if not name:
                print("Error: Product name cannot be empty.")

            elif name.casefold() in {
                product.casefold()
                for product in product_names
            }:
                print("Error: Product name already exists.")

            else:
                break

        prices = []

        for period in range(period_count):
            price = read_positive_number(
                f"Enter price for period {period + 1}: "
            )

            prices.append(price)

        product_names.append(name)
        price_history.append(prices)

    return product_names, price_history


def calculate_percentage_changes(prices):
    """Calculate percentage changes between consecutive prices."""
    changes = []

    for index in range(1, len(prices)):
        previous_price = prices[index - 1]
        current_price = prices[index]

        percentage = (
            (current_price - previous_price)
            / previous_price
        ) * 100

        changes.append(percentage)

    return changes


def analyse_price_fluctuations(
    product_names, price_history, threshold
):
    """Analyse fluctuations and flag products."""
    report = []

    for name, prices in zip(product_names, price_history):
        changes = calculate_percentage_changes(prices)

        maximum_fluctuation = max(
            abs(change) for change in changes
        )

        flagged = maximum_fluctuation > threshold

        report.append({
            "name": name,
            "prices": prices,
            "changes": changes,
            "maximum_fluctuation": maximum_fluctuation,
            "flagged": flagged
        })

    return report


def display_report(report, threshold):
    """Display the final price fluctuation report."""
    print("\n========== PRICE FLUCTUATION REPORT ==========")
    print(f"Fluctuation Threshold: {threshold:.2f}%")

    for item in report:
        print(f"\nProduct: {item['name']}")
        print(f"Historical Prices: {item['prices']}")

        print("Percentage Changes:")

        for index, change in enumerate(
            item["changes"], start=1
        ):
            print(
                f"Period {index} to Period {index + 1}: "
                f"{change:+.2f}%"
            )

        print(
            f"Maximum Fluctuation: "
            f"{item['maximum_fluctuation']:.2f}%"
        )

        status = "FLAGGED" if item["flagged"] else "WITHIN THRESHOLD"
        print(f"Status: {status}")

    highest = max(
        report,
        key=lambda item: item["maximum_fluctuation"]
    )

    flagged_products = [
        item["name"]
        for item in report
        if item["flagged"]
    ]

    print("\n========== FINAL ANALYSIS ==========")
    print(f"Highest Fluctuation Product: {highest['name']}")
    print(
        f"Maximum Fluctuation: "
        f"{highest['maximum_fluctuation']:.2f}%"
    )

    print(f"Flagged Products: {flagged_products}")


def main():
    print("MULTI-PRODUCT PRICE FLUCTUATION ANALYSIS")

    product_count = read_positive_integer(
        "Enter number of products: "
    )

    period_count = read_positive_integer(
        "Enter number of historical periods (minimum 2): "
    )

    while period_count < 2:
        print("Error: At least two periods are required.")
        period_count = read_positive_integer(
            "Enter number of historical periods: "
        )

    threshold = read_threshold()

    product_names, price_history = collect_product_data(
        product_count, period_count
    )

    report = analyse_price_fluctuations(
        product_names, price_history, threshold
    )

    display_report(report, threshold)


if __name__ == "__main__":
    main()