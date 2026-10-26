
# Comprehensive Smart Campus Management System

# Student records: [Roll No, Name, Department]
students = [
    [101, "Arun", "CSE"],
    [102, "Priya", "ECE"],
    [103, "Rahul", "CSE"]
]

# Attendance records: [Roll No, Classes Attended, Total Classes]
attendance = [
    [101, 18, 20],
    [102, 16, 20],
    [103, 14, 20]
]

# Marks records: [Roll No, Subject, Marks]
marks = [
    [101, "Python", 85],
    [102, "Python", 78],
    [103, "Python", 65]
]

# Events and registered student roll numbers
events = {
    "Tech Fest": [],
    "Sports Day": [],
    "Coding Contest": []
}

# Resource name and availability
resources = {
    "Computer Lab": 2,
    "Seminar Hall": 1,
    "Projector": 3
}


def find_student(roll_no):
    for student in students:
        if student[0] == roll_no:
            return student
    return None


def display_students():
    print("\n--- Student Records ---")
    for roll_no, name, department in students:
        print(f"Roll No: {roll_no}, Name: {name}, "
              f"Department: {department}")


def record_attendance():
    roll_no = int(input("Enter roll number: "))
    student = find_student(roll_no)

    if student is None:
        print("Student not found.")
        return

    attended = int(input("Enter classes attended: "))
    total = int(input("Enter total classes: "))

    if total <= 0 or attended < 0 or attended > total:
        print("Invalid attendance details.")
        return

    for record in attendance:
        if record[0] == roll_no:
            record[1] = attended
            record[2] = total
            break
    else:
        attendance.append([roll_no, attended, total])

    percentage = attended / total * 100
    print(f"Attendance: {percentage:.2f}%")
    print("Attendance updated successfully.")


def record_marks():
    roll_no = int(input("Enter roll number: "))
    student = find_student(roll_no)

    if student is None:
        print("Student not found.")
        return

    subject = input("Enter subject: ").strip()
    score = float(input("Enter marks (0-100): "))

    if not subject or not 0 <= score <= 100:
        print("Invalid subject or marks.")
        return

    for record in marks:
        if record[0] == roll_no and record[1].lower() == subject.lower():
            record[2] = score
            break
    else:
        marks.append([roll_no, subject, score])

    print("Marks recorded successfully.")


def register_event():
    roll_no = int(input("Enter student roll number: "))
    student = find_student(roll_no)

    if student is None:
        print("Student not found.")
        return

    print("Available events:")
    for event_name in events:
        print("-", event_name)

    event_name = input("Enter event name: ").strip()

    if event_name not in events:
        print("Event not found.")
    elif roll_no in events[event_name]:
        print("Student is already registered.")
    else:
        events[event_name].append(roll_no)
        print(f"{student[1]} registered for {event_name}.")


def allocate_resource():
    print("\nAvailable resources:")
    for resource, quantity in resources.items():
        print(f"{resource}: {quantity} available")

    resource = input("Enter resource name: ").strip()

    if resource not in resources:
        print("Resource not found.")
    elif resources[resource] > 0:
        resources[resource] -= 1
        print(f"{resource} allocated successfully.")
        print(f"Remaining: {resources[resource]}")
    else:
        print("Sorry, this resource is unavailable.")


def summary_report():
    print("\n========== CAMPUS SUMMARY ==========")
    print("Total students:", len(students))
    print("Total attendance records:", len(attendance))
    print("Total marks records:", len(marks))

    print("\nStudent Performance:")
    for roll_no, name, department in students:
        student_marks = [
            record[2] for record in marks
            if record[0] == roll_no
        ]

        if student_marks:
            average = sum(student_marks) / len(student_marks)
            print(f"{name} ({department}) - Average: {average:.2f}")
        else:
            print(f"{name} ({department}) - No marks recorded")

    print("\nAttendance Report:")
    for roll_no, attended, total in attendance:
        student = find_student(roll_no)
        if student and total > 0:
            percentage = attended / total * 100
            print(f"{student[1]} - {percentage:.2f}%")

    print("\nEvent Registrations:")
    for event_name, registered_students in events.items():
        print(f"{event_name}: {len(registered_students)} students")

    print("\nResource Availability:")
    for resource, quantity in resources.items():
        print(f"{resource}: {quantity} available")

    print("====================================")


def main():
    while True:
        print("\n===== SMART CAMPUS MANAGEMENT =====")
        print("1. Display Student Records")
        print("2. Update Attendance")
        print("3. Record Student Marks")
        print("4. Register for an Event")
        print("5. Allocate Campus Resource")
        print("6. Generate Summary Report")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_students()
        elif choice == "2":
            record_attendance()
        elif choice == "3":
            record_marks()
        elif choice == "4":
            register_event()
        elif choice == "5":
            allocate_resource()
        elif choice == "6":
            summary_report()
        elif choice == "7":
            print("Thank you for using Smart Campus Management!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
