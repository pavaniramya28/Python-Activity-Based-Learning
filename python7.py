
# Multi-Product Price Fluctuation Analysis System

# Historical prices of products
product_prices = {
    "Laptop": [50000, 52000, 49000, 55000],
    "Mobile": [20000, 21000, 23000, 22000],
    "Headphones": [2000, 1900, 2100, 2500],
    "Keyboard": [1500, 1550, 1520, 1600]
}

# Maximum acceptable percentage fluctuation
FLUCTUATION_THRESHOLD = 10.0


def calculate_percentage_changes(prices):
    """Calculate percentage changes between consecutive prices."""
    changes = []

    for previous, current in zip(prices, prices[1:]):
        if previous <= 0:
            changes.append(None)
        else:
            percentage = ((current - previous) / previous) * 100
            changes.append(percentage)

    return changes


def analyse_products(products, threshold):
    """Analyse product prices and identify significant fluctuations."""
    results = {}

    for product, prices in products.items():
        if len(prices) < 2:
            results[product] = {
                "changes": [],
                "max_fluctuation": None,
                "flagged": False,
                "error": "At least two prices are required."
            }
            continue

        if any(price <= 0 for price in prices):
            results[product] = {
                "changes": [],
                "max_fluctuation": None,
                "flagged": False,
                "error": "All prices must be positive."
            }
            continue

        changes = calculate_percentage_changes(prices)

        # Largest change by absolute percentage
        max_fluctuation = max(changes, key=abs)

        # Flag if any price change exceeds the threshold
        flagged = any(abs(change) > threshold for change in changes)

        results[product] = {
            "changes": changes,
            "max_fluctuation": max_fluctuation,
            "flagged": flagged
        }

    return results


def display_report(results, threshold):
    """Display the price fluctuation report."""
    print("\nMULTI-PRODUCT PRICE FLUCTUATION REPORT")
    print("=" * 65)
    print(f"Fluctuation threshold: {threshold:.2f}%")

    for product, data in results.items():
        print(f"\nProduct: {product}")

        if "error" in data:
            print(f"Status: {data['error']}")
            continue

        print("Percentage changes:")

        for index, change in enumerate(data["changes"], start=1):
            print(f"  Period {index}: {change:+.2f}%")

        maximum = data["max_fluctuation"]

        print(f"Maximum fluctuation: {abs(maximum):.2f}%")
        print(f"Direction: {'Increase' if maximum > 0 else 'Decrease' if maximum < 0 else 'No change'}")

        if data["flagged"]:
            print("Alert: EXCEEDS THRESHOLD")
        else:
            print("Status: Within threshold")

    valid_results = {
        product: data
        for product, data in results.items()
        if "error" not in data
    }

    if valid_results:
        most_volatile = max(
            valid_results,
            key=lambda product: abs(
                valid_results[product]["max_fluctuation"]
            )
        )

        print("\n" + "=" * 65)
        print(f"Most volatile product: {most_volatile}")
        print(
            "Maximum fluctuation: "
            f"{abs(valid_results[most_volatile]['max_fluctuation']):.2f}%"
        )


def main():
    results = analyse_products(
        product_prices,
        FLUCTUATION_THRESHOLD
    )

    display_report(results, FLUCTUATION_THRESHOLD)


if __name__ == "__main__":
    main()
