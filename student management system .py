students = []

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    students.append({"name": name, "age": age})
    print("✅ Student added successfully!")

def view_students():
    if not students:
        print("❌ No students found")
    else:
        print("\n📋 Student List:")
        for i, s in enumerate(students):
            print(f"{i+1}. Name: {s['name']} | Age: {s['age']}")

def update_student():
    view_students()
    try:
        index = int(input("Enter student number to update: ")) - 1
        if 0 <= index < len(students):
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            students[index] = {"name": name, "age": age}
            print(" Student updated successfully!")
        else:
            print(" Invalid number")
    except:
        print("Enter valid input")

def delete_student():
    view_students()
    try:
        index = int(input("Enter student number to delete: ")) - 1
        if 0 <= index < len(students):
            students.pop(index)
            print(" Student deleted successfully!")
        else:
            print("Invalid number")
    except:
        print(" Enter valid input")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print(" Exiting program...")
        break
    else:
        print("❌ Invalid choice, try again")
