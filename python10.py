# COMPREHENSIVE SMART CAMPUS MANAGEMENT SYSTEM

# Campus records
students = {}
attendance_records = {}
marks_records = {}

events = {
    "Technical Fest": [50, []],
    "Cultural Fest": [40, []],
    "Sports Meet": [30, []]
}

resources = {
    "Projector": [10, 0],
    "Computer": [50, 0],
    "Laboratory": [5, 0]
}


def read_integer(message, minimum=0):
    """Read and validate an integer."""
    while True:
        try:
            value = int(input(message))

            if value >= minimum:
                return value

            print(f"Error: Enter a value of at least {minimum}.")

        except ValueError:
            print("Error: Enter a valid integer.")


def read_non_empty_string(message):
    """Read a non-empty string."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Error: This field cannot be empty.")


def find_student(student_id):
    """Check whether a student exists."""
    return student_id in students


# --------------------------------------------------
# 1. STUDENT MANAGEMENT
# --------------------------------------------------

def add_student():
    """Add a new student to campus records."""
    print("\n========== STUDENT REGISTRATION ==========")

    student_id = read_non_empty_string("Enter student ID: ")

    if find_student(student_id):
        print("Error: Student ID already exists.")
        return

    name = read_non_empty_string("Enter student name: ")

    department = read_non_empty_string(
        "Enter department: "
    )

    year = read_integer("Enter academic year: ", 1)

    if year > 4:
        print("Error: Academic year must be between 1 and 4.")
        return

    # Store student information as a tuple.
    students[student_id] = (name, department, year)

    attendance_records[student_id] = [0, 0]
    marks_records[student_id] = []

    print("Student registered successfully.")


# --------------------------------------------------
# 2. ATTENDANCE MANAGEMENT
# --------------------------------------------------

def update_attendance():
    """Update attendance information."""
    print("\n========== ATTENDANCE MANAGEMENT ==========")

    student_id = read_non_empty_string("Enter student ID: ")

    if not find_student(student_id):
        print("Error: Student record not found.")
        return

    total_sessions = read_integer(
        "Enter additional total sessions: ", 1
    )

    attended_sessions = read_integer(
        "Enter attended sessions: "
    )

    if attended_sessions > total_sessions:
        print("Error: Attended sessions cannot exceed total sessions.")
        return

    attendance = attendance_records[student_id]

    attendance[0] += attended_sessions
    attendance[1] += total_sessions

    attended, total = attendance

    percentage = (attended / total) * 100

    print("Attendance updated successfully.")
    print(f"Attendance Percentage: {percentage:.2f}%")


# --------------------------------------------------
# 3. MARKS MANAGEMENT
# --------------------------------------------------

def add_marks():
    """Add subject-wise examination marks."""
    print("\n========== MARKS MANAGEMENT ==========")

    student_id = read_non_empty_string("Enter student ID: ")

    if not find_student(student_id):
        print("Error: Student record not found.")
        return

    subject = read_non_empty_string("Enter subject name: ")

    if any(
        record[0].casefold() == subject.casefold()
        for record in marks_records[student_id]
    ):
        print("Error: Marks for this subject already exist.")
        return

    marks = read_integer("Enter marks (0-100): ")

    if marks > 100:
        print("Error: Marks cannot exceed 100.")
        return

    # Each record is a nested list containing subject and marks.
    marks_records[student_id].append([subject, marks])

    print("Marks added successfully.")


# --------------------------------------------------
# 4. EVENT REGISTRATION
# --------------------------------------------------

def register_event():
    """Register a student for a campus event."""
    print("\n========== EVENT REGISTRATION ==========")

    student_id = read_non_empty_string("Enter student ID: ")

    if not find_student(student_id):
        print("Error: Student record not found.")
        return

    print("\nAvailable Events:")

    for event_name, (capacity, registered_students) in events.items():
        available = capacity - len(registered_students)

        print(
            f"{event_name} - "
            f"Available Seats: {available}"
        )

    event_name = read_non_empty_string(
        "Enter event name: "
    )

    if event_name not in events:
        print("Error: Event does not exist.")
        return

    capacity, registered_students = events[event_name]

    if student_id in registered_students:
        print("Error: Student already registered for this event.")
        return

    if len(registered_students) >= capacity:
        print("Error: Event registration is full.")
        return

    registered_students.append(student_id)

    print(f"Successfully registered for {event_name}.")


# --------------------------------------------------
# 5. RESOURCE ALLOCATION
# --------------------------------------------------

def allocate_resource():
    """Allocate campus resources."""
    print("\n========== RESOURCE ALLOCATION ==========")

    print("\nAvailable Resources:")

    for resource_name, (capacity, allocated) in resources.items():
        print(
            f"{resource_name}: "
            f"Total = {capacity}, "
            f"Allocated = {allocated}, "
            f"Available = {capacity - allocated}"
        )

    resource_name = read_non_empty_string(
        "Enter resource name: "
    )

    if resource_name not in resources:
        print("Error: Resource does not exist.")
        return

    quantity = read_integer(
        "Enter required quantity: ", 1
    )

    capacity, allocated = resources[resource_name]

    available = capacity - allocated

    if quantity > available:
        print("Error: Insufficient resources available.")
        return

    resources[resource_name][1] += quantity

    print("Resource allocated successfully.")


# --------------------------------------------------
# 6. CAMPUS SUMMARY REPORT
# --------------------------------------------------

def display_summary():
    """Display integrated campus information."""
    print("\n========== SMART CAMPUS SUMMARY ==========")

    print("\nSTUDENT RECORDS")

    if not students:
        print("No student records available.")

    for student_id, student_record in students.items():

        # Tuple unpacking
        name, department, year = student_record

        print(
            f"\nID: {student_id} | "
            f"Name: {name} | "
            f"Department: {department} | "
            f"Year: {year}"
        )

        attended, total = attendance_records[student_id]

        if total > 0:
            percentage = (attended / total) * 100
        else:
            percentage = 0.0

        print(
            f"Attendance: {attended}/{total} "
            f"({percentage:.2f}%)"
        )

        print("Marks:")

        if marks_records[student_id]:
            for subject, marks in marks_records[student_id]:
                print(f"  {subject}: {marks}/100")
        else:
            print("  No marks available.")

    print("\nEVENT REGISTRATION SUMMARY")

    for event_name, (capacity, registered_students) in events.items():
        print(
            f"{event_name}: "
            f"{len(registered_students)}/{capacity} registered"
        )

    print("\nRESOURCE ALLOCATION SUMMARY")

    for resource_name, (capacity, allocated) in resources.items():
        print(
            f"{resource_name}: "
            f"Allocated = {allocated}, "
            f"Available = {capacity - allocated}"
        )

    print("\n========== END OF SUMMARY ==========")


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def display_menu():
    """Display available campus operations."""
    print("\n========================================")
    print("     SMART CAMPUS MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Student Management")
    print("2. Attendance Management")
    print("3. Marks Management")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Campus Summary Report")
    print("0. Exit")
    print("========================================")


def main():
    """Control the complete campus management system."""

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            update_attendance()

        elif choice == "3":
            add_marks()

        elif choice == "4":
            register_event()

        elif choice == "5":
            allocate_resource()

        elif choice == "6":
            display_summary()

        elif choice == "0":
            print("\nThank you for using Smart Campus Management System.")
            break

        else:
            print("Invalid choice. Please select a valid menu option.")


if __name__ == "__main__":
    main()