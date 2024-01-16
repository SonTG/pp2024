class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        
def get_student_infor():
    student_id = input("Enter student ID :")
    student_name = input("Enter student name :")
    student_dob = input("Enter student date of birth (YYYY-MM-DD): ")
    return student_id,student_name
def input_course_info():
    num_courses = int(input("Enter the number of course :"))
    courses = []
    for i in range(num_courses):
        course_id=input("Enter Course code:")
        course_name = input("Enter course name :")
        courses.append(Course(course_id,course_name))
    return courses

def input_marks(students, course):
    selected_course_id = input("Select a course ID to inpt marks :  ")
    for course in Course:
        if course.course_id == selected_course_id:
            for student in students:
                marks = float(input(f"Enter marks for {student.name} in {course.name}: "))

