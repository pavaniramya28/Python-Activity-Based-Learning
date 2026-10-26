
# Water Distribution Fairness Analysis System

# Daily water demand for each area (in litres)
water_demand = {
    "Area A": 1000,
    "Area B": 1200,
    "Area C": 800,
    "Area D": 1500
}

# Water supplied to each area over multiple days (in litres)
water_supply = {
    "Area A": [900, 850, 950],
    "Area B": [1000, 900, 950],
    "Area C": [800, 800, 750],
    "Area D": [1000, 1100, 900]
}


def analyse_water_distribution(demand, supply):
    """Calculate shortages and distribution fairness."""

    results = {}

    for area, daily_supply in supply.items():
        required = demand[area] * len(daily_supply)
        total_supplied = sum(daily_supply)
        shortage = max(0, required - total_supplied)
        excess = max(0, total_supplied - required)

        fulfilment = (
            total_supplied / required * 100
            if required > 0 else 0
        )

        results[area] = {
            "demand": required,
            "supply": total_supplied,
            "shortage": shortage,
            "excess": excess,
            "fulfilment": fulfilment
        }

    return results


def display_report(results):
    """Display area-wise water distribution statistics."""

    print("\nWATER DISTRIBUTION FAIRNESS REPORT")
    print("=" * 78)

    print(
        f"{'Area':<10}{'Demand':>12}{'Supply':>12}"
        f"{'Shortage':>12}{'Fulfilment':>14}"
    )
    print("-" * 78)

    for area, data in results.items():
        print(
            f"{area:<10}{data['demand']:>12}"
            f"{data['supply']:>12}{data['shortage']:>12}"
            f"{data['fulfilment']:>13.2f}%"
        )

    # Identify the most underserved area
    most_underserved = min(
        results,
        key=lambda area: results[area]["fulfilment"]
    )

    # Compare areas using their fulfilment percentages
    best_served = max(
        results,
        key=lambda area: results[area]["fulfilment"]
    )

    print("\nCOMPARISON")
    print("-" * 40)
    print(f"Most underserved area: {most_underserved}")
    print(
        "Fulfilment percentage: "
        f"{results[most_underserved]['fulfilment']:.2f}%"
    )
    print(f"Best-served area: {best_served}")
    print(
        "Fulfilment percentage: "
        f"{results[best_served]['fulfilment']:.2f}%"
    )

    total_shortage = sum(
        data["shortage"] for data in results.values()
    )
    print(f"\nTotal water shortage: {total_shortage} litres")


def main():
    results = analyse_water_distribution(
        water_demand,
        water_supply
    )

    display_report(results)


if __name__ == "__main__":
    main()
