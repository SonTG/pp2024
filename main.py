class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class Class:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def add_marks(self, student_id, course_id, marks):
        for student in self.students:
            if student.student_id == student_id:
                student.marks[course_id] = marks
                break

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_marks(self, student_id, course_id):
        for student in self.students:
            if student.student_id == student_id:
                if course_id in student.marks:
                    marks = student.marks[course_id]
                    print(f"Student ID: {student_id}, Course ID: {course_id}, Marks: {marks}")
                else:
                    print("Marks not available for the given course.")
                break


# Example usage
my_class = Class()

# Input number of students
num_students = int(input("Enter the number of students: "))

# Input student information
for _ in range(num_students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    student = Student(student_id, name, dob)
    my_class.add_student(student)

# Input number of courses
num_courses = int(input("Enter the number of courses: "))

# Input course information
for _ in range(num_courses):
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    course = Course(course_id, name)
    my_class.add_course(course)

# Select a course and input marks
my_class.list_courses()
course_id = input("Enter the course ID to input marks: ")
my_class.list_students()
student_id = input("Enter the student ID to input marks: ")
marks = float(input("Enter the marks for the student: "))
my_class.add_marks(student_id, course_id, marks)

# List courses
my_class.list_courses()

# List students
my_class.list_students()

# Show student marks for a given course
course_id = input("Enter the course ID to show marks: ")
student_id = input("Enter the student ID to show marks: ")
my_class.show_marks(student_id, course_id)