def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return (student_id, student_name, student_dob)

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return (course_id, course_name)

# Other functions remain the same

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
        marks[course_info[0]] = {}  # Using course ID as keys for marks dictionary

    # Remaining code remains unchanged

if __name__ == "__main__":
    main()
