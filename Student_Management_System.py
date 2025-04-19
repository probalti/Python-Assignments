# Student Management System

students = []

def add_student(student_id, name, age, shift):
    """Add a new student to the list."""
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "shift": shift
    }
    students.append(student)
    print(f"Student {name} added successfully!")

def view_students():
    """Display all students."""
    if not students:
        print("No students found.")
        return
    print("\nStudent List:")
    print("ID\tName\t\tAge\tShift")
    print("-" * 40)
    for student in students:
        print(f"{student['id']}\t{student['name']:<15}\t{student['age']}\t{student['shift']}")

def update_student(student_id):
    """Update a student's details."""
    for student in students:
        if student["id"] == student_id:
            print(f"Updating student: {student['name']}")
            name = input("Enter new name (or press Enter to keep unchanged): ")
            age = input("Enter new age (or press Enter to keep unchanged): ")
            shift = input("Enter new shift (e.g., Saturday 9-12) (or press Enter to keep unchanged): ")
            
            if name:
                student["name"] = name
            if age and age.isdigit():
                student["age"] = int(age)
            if shift:
                student["shift"] = shift
            print("Student updated successfully!")
            return
    print(f"Student with ID {student_id} not found.")

def delete_student(student_id):
    """Delete a student by ID."""
    for i, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(i)
            print(f"Student {deleted_student['name']} deleted successfully!")
            return
    print(f"Student with ID {student_id} not found.")

def main():
    """Main function to run the student management system."""
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            student_id = input("Enter student ID: ")
            # Check if ID already exists
            if any(student["id"] == student_id for student in students):
                print("Student ID already exists!")
                continue
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            if not age.isdigit():
                print("Invalid age! Age must be a number.")
                continue
            age = int(age)
            shift = input("Enter student shift (e.g., Saturday 9-12): ")
            add_student(student_id, name, age, shift)
        
        elif choice == "2":
            view_students()
        
        elif choice == "3":
            student_id = input("Enter student ID to update: ")
            update_student(student_id)
        
        elif choice == "4":
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
        
        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()