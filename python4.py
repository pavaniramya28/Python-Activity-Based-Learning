
# Student Timetable Conflict Detection System

from datetime import datetime


# Unavailable rooms
UNAVAILABLE_ROOMS = {"R101", "R202"}

# Existing timetable: (day, start_time, end_time, room, course)
EXISTING_TIMETABLE = [
    ("Monday", "09:00", "10:00", "R101", "Python"),
    ("Monday", "10:00", "11:00", "R103", "Mathematics"),
    ("Tuesday", "11:00", "12:00", "R104", "Database")
]


def time_to_minutes(time_string):
    """Convert HH:MM time into minutes."""
    parsed_time = datetime.strptime(time_string, "%H:%M")
    return parsed_time.hour * 60 + parsed_time.minute


def validate_entry(entry):
    """Validate the structure and timing of a timetable entry."""
    day, start, end, room, course = entry

    if not all(isinstance(value, str) and value.strip()
               for value in entry):
        return "All fields must contain valid non-empty strings."

    try:
        start_minutes = time_to_minutes(start)
        end_minutes = time_to_minutes(end)
    except ValueError:
        return "Invalid time format. Use HH:MM."

    if start_minutes >= end_minutes:
        return "End time must be later than start time."

    return None


def detect_conflicts(proposed_timetable):
    """Detect time overlaps, unavailable rooms and invalid entries."""
    errors = []

    for index, entry in enumerate(proposed_timetable):
        problem = validate_entry(entry)

        if problem:
            errors.append(
                f"Entry {index + 1} ({entry[4]}): {problem}"
            )

    # Check valid entries only
    valid_entries = [
        entry for entry in proposed_timetable
        if validate_entry(entry) is None
    ]

    # Check unavailable rooms
    for day, start, end, room, course in valid_entries:
        if room in UNAVAILABLE_ROOMS:
            errors.append(
                f"{course}: Room {room} is unavailable."
            )

    # Check overlapping periods between courses
    for i in range(len(valid_entries)):
        day1, start1, end1, room1, course1 = valid_entries[i]

        for j in range(i + 1, len(valid_entries)):
            day2, start2, end2, room2, course2 = valid_entries[j]

            # Classes on different days cannot overlap
            if day1.lower() != day2.lower():
                continue

            start1_min = time_to_minutes(start1)
            end1_min = time_to_minutes(end1)
            start2_min = time_to_minutes(start2)
            end2_min = time_to_minutes(end2)

            # Two periods overlap if each starts before the other ends
            if start1_min < end2_min and start2_min < end1_min:
                errors.append(
                    f"Time conflict: {course1} ({start1}-{end1}) "
                    f"and {course2} ({start2}-{end2}) "
                    f"overlap on {day1}."
                )

    return errors


def display_report(timetable, errors):
    """Display the proposed timetable and validation result."""
    print("\nSTUDENT TIMETABLE CONFLICT REPORT")
    print("=" * 55)

    for entry in timetable:
        day, start, end, room, course = entry
        print(
            f"{day:10} | {start}-{end} | "
            f"{room:5} | {course}"
        )

    print("\nVALIDATION RESULTS")
    print("-" * 55)

    if errors:
        for number, error in enumerate(errors, start=1):
            print(f"{number}. {error}")

        print("\nTimetable Status: INVALID")
    else:
        print("No conflicts detected.")
        print("Timetable Status: VALID")


def main():
    # Proposed timetable represented using tuples
    proposed_timetable = [
        ("Monday", "09:30", "10:30", "R105", "Python Lab"),
        ("Monday", "10:15", "11:15", "R103", "Web Development"),
        ("Tuesday", "12:00", "13:00", "R106", "Computer Networks")
    ]

    errors = detect_conflicts(proposed_timetable)
    display_report(proposed_timetable, errors)


if __name__ == "__main__":
    main()
