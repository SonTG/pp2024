import math

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

    def add_marks(self, student_id, course_id, marks):
        for student in self.students:
            if student.student_id == student_id:
                rounded_marks = math.floor(marks * 10) / 10  # Round down to 1-digit decimal
                student.marks[course_id] = rounded_marks
                break
