students_grades = {
    "Haris": [],
    "Shaheer": [],
    "Ali": []
}

def add_grade():
    student_name = input("Enter the name of the student to add a grade to: ")
    if student_name in students_grades:
        grade = int(input(f"Enter the grade to add for {student_name}: "))
        students_grades[student_name].append(grade)
        print(f"Added grade {grade} to {student_name}.")
    else:
        print(f"Student {student_name} not found.")

def calculate_average(student_name):
    if student_name in students_grades:
        grades = students_grades[student_name]
        if grades:
            average = sum(grades) / len(grades)
            print(f"{student_name}'s average grade is: {average:.2f}")
        else:
            print(f"{student_name} has no grades recorded.")
    else:
        print(f"Student {student_name} not found.")

def add_student():
    student_name = input("Enter the name of the new student: ")
    if student_name not in students_grades:
        students_grades[student_name] = []
        print(f"Added new student: {student_name}.")
    else:
        print(f"Student {student_name} already exists.")

def remove_student():
    student_name = input("Enter the name of the student to remove: ")
    if student_name in students_grades:
        del students_grades[student_name]
        print(f"Removed student: {student_name}.")
    else:
        print(f"Student {student_name} not found.")

def input_grades():
    for student in students_grades.keys():
        grades_input = input(f"Enter grades for {student} separated by spaces: ")
        grades = list(map(int, grades_input.split()))
        students_grades[student].extend(grades)
        print(f"Grades {grades} added for {student}.")

while True:
    print("\nMenu:")
    print("1. Add a new student")
    print("2. Remove a student")
    print("3. Add grades for an existing student")
    print("4. Calculate average grade for a student")
    print("5. Enter initial grades for all students")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        add_grade()
    elif choice == "4":
        student_name = input("Enter the name of the student to calculate the average for: ")
        calculate_average(student_name)
    elif choice == "5":
        input_grades()
    elif choice == "6":
        break
    else:
        print("Invalid option, please try again.")

print("\nUpdated student grades:", students_grades)
