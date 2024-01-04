def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_info = {}
    student_info['id'] = input("Enter student ID: ")
    student_info['name'] = input("Enter student name: ")
    student_info['dob'] = input("Enter student date of birth: ")
    return student_info

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_info = {}
    course_info['id'] = input("Enter course ID: ")
    course_info['name'] = input("Enter course name: ")
    return course_info

def input_marks(students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student['name']}: "))
        marks[student['id']] = mark
    return marks

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}")

def show_student_marks(students, marks, course_id):
    print(f"Student marks for course ID {course_id}:")
    for student in students:
        if student['id'] in marks[course_id]:
            print(f"ID: {student['id']}, Name: {student['name']}, Mark: {marks[course_id][student['id']]}")
        else:
            print(f"ID: {student['id']}, Name: {student['name']}, Mark: Not available")

def main():
    students = []
    courses = []
    marks = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        student_info = input_student_info()
        students.append(student_info)

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_info = input_course_info()
        courses.append(course_info)
        marks[course_info['id']] = {}

    while True:
        print("\nMenu:")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_courses(courses)
        elif choice == 2:
            list_students(students)
        elif choice == 3:
            course_id = input("Enter course ID to input marks: ")
            if course_id in marks:
                marks[course_id] = input_marks(students)
            else:
                print("Invalid course ID")
        elif choice == 4:
            course_id = input("Enter course ID to show marks: ")
            if course_id in marks:
                show_student_marks(students, marks, course_id)
            else:
                print("Invalid course ID")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
