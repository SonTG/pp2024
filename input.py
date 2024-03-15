import numpy as np

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
    def calculate_gpa(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                if len(student.marks) == 0:
                    return 0.0  # No marks available
                else:
                    marks = np.array(list(student.marks.values()))
                    credits = np.array([course.credits for course in self.courses])
                    weighted_avg = np.dot(marks, credits) / np.sum(credits)
                    gpa = np.round(weighted_avg, decimals=1)
                    return gpa
        return 0.0  # Student not found

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: self.calculate_gpa(student.student_id), reverse=True)