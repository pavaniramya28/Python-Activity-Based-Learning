def read_positive_integer(message):
    """Read a positive integer from the user."""
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Error: Enter a value greater than zero.")

        except ValueError:
            print("Error: Enter a valid integer.")


def read_non_negative_number(message):
    """Read a non-negative water quantity."""
    while True:
        try:
            value = float(input(message))

            if value >= 0:
                return value

            print("Error: Quantity cannot be negative.")

        except ValueError:
            print("Error: Enter a valid numeric value.")


def read_area_name(existing_names):
    """Read a unique area name."""
    while True:
        name = input("Enter area name: ").strip()

        if not name:
            print("Error: Area name cannot be empty.")

        elif name.casefold() in existing_names:
            print("Error: Area name already exists.")

        else:
            return name


def collect_water_data(area_count, day_count):
    """Collect demand and supply data for all areas."""
    area_names = []
    demands = []
    supplies = []

    for area_index in range(area_count):
        print(f"\nAREA {area_index + 1}")

        name = read_area_name(
            {area.casefold() for area in area_names}
        )

        daily_demand = []
        daily_supply = []

        for day in range(day_count):
            print(f"\nDay {day + 1}")

            demand = read_non_negative_number(
                "Enter water demand (litres): "
            )

            supply = read_non_negative_number(
                "Enter water supplied (litres): "
            )

            daily_demand.append(demand)
            daily_supply.append(supply)

        area_names.append(name)
        demands.append(daily_demand)
        supplies.append(daily_supply)

    return area_names, demands, supplies


def analyse_distribution(area_names, demands, supplies):
    """Calculate area-wise water distribution statistics."""
    report = []

    for index, area in enumerate(area_names):
        total_demand = sum(demands[index])
        total_supply = sum(supplies[index])

        daily_shortages = [
            max(0, demand - supply)
            for demand, supply in zip(
                demands[index], supplies[index]
            )
        ]

        total_shortage = sum(daily_shortages)

        if total_demand > 0:
            shortage_percentage = (
                total_shortage / total_demand
            ) * 100
        else:
            shortage_percentage = 0.0

        if total_demand > 0:
            fulfilment_percentage = (
                min(total_supply, total_demand)
                / total_demand
            ) * 100
        else:
            fulfilment_percentage = 100.0

        report.append({
            "area": area,
            "demand": total_demand,
            "supply": total_supply,
            "shortage": total_shortage,
            "shortage_percentage": shortage_percentage,
            "fulfilment_percentage": fulfilment_percentage,
            "daily_shortages": daily_shortages
        })

    return report


def display_report(report):
    """Display the water distribution analysis."""
    print("\n========== WATER DISTRIBUTION REPORT ==========")

    print(
        f"{'Area':<12}{'Demand':>12}{'Supply':>12}"
        f"{'Shortage':>12}{'Shortage %':>14}"
    )

    print("-" * 62)

    for item in report:
        print(
            f"{item['area']:<12}"
            f"{item['demand']:>12.2f}"
            f"{item['supply']:>12.2f}"
            f"{item['shortage']:>12.2f}"
            f"{item['shortage_percentage']:>13.2f}%"
        )

    print("\n========== DISTRIBUTION COMPARISON ==========")

    for item in report:
        print(
            f"{item['area']}: "
            f"Fulfilment = {item['fulfilment_percentage']:.2f}%"
        )

    most_underserved = max(
        report,
        key=lambda item: item["shortage_percentage"]
    )

    print("\nMost Underserved Area:")
    print(f"Area: {most_underserved['area']}")
    print(
        f"Shortage Percentage: "
        f"{most_underserved['shortage_percentage']:.2f}%"
    )


def main():
    print("WATER DISTRIBUTION FAIRNESS ANALYSIS")

    area_count = read_positive_integer("Enter number of areas: ")
    day_count = read_positive_integer("Enter number of days: ")

    area_names, demands, supplies = collect_water_data(
        area_count, day_count
    )

    report = analyse_distribution(
        area_names, demands, supplies
    )

    display_report(report)


if __name__ == "__main__":
    main()