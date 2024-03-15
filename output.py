import curses
import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

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
                rounded_marks = math.floor(marks * 10) / 10  # Round down to 1-digit decimal
                student.marks[course_id] = rounded_marks
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


def main(stdscr):
    # Initialization
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    stdscr.keypad(1)

    # Create a class instance
    my_class = Class()

    while True:
        stdscr.clear()
        stdscr.addstr("1. Add Student\n")
        stdscr.addstr("2. Add Course\n")
        stdscr.addstr("3. Add Marks\n")
        stdscr.addstr("4. Calculate GPA\n")
        stdscr.addstr("5. Sort Students by GPA\n")
        stdscr.addstr("6. Quit\n")
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            stdscr.clear()
            stdscr.addstr("Add Student\n\n")
            stdscr.addstr("Enter student ID: ")
            student_id = stdscr.getstr().decode("utf-8")
            stdscr.addstr("Enter name: ")
            name = stdscr.getstr().decode("utf-8")
            stdscr.addstr("Enter date of birth: ")
            dob = stdscr.getstr().decode("utf-8")
            student = Student(student_id, name, dob)
            my_class.add_student(student)

        elif key == ord('2'):
            stdscr.clear()
            stdscr.addstr("Add Course\n\n")
            stdscr.addstr("Enter course ID: ")
            course_id = stdscr.getstr().decode("utf-8")
            stdscr.addstr("Enter name: ")
            name = stdscr.getstr().decode("utf-8")
            stdscr.addstr("Enter credits: ")
            credits = int(stdscr.getstr().decode("utf-8"))
            course = Course(course_id, name, credits)
            my_class.add_course(course)

        elif key == ord('3'):
            stdscr.clear()
            stdscr.addstr("Add Marks\n\n")
            stdscr.addstr("Select a course:\n")
            for i, course in enumerate(my_class.courses):
                stdscr.addstr(f"{i+1}. {course.name}\n")
            course_index = int(stdscr.getstr().decode("utf-8")) - 1
            selected_course = my_class.courses[course_index]

            stdscr.addstr("Select a student:\n")
            for i, student in enumerate(my_class.students):
                stdscr.addstr(f"{i+1}. {student.name}\n")
            student_index = int(stdscr.getstr().decode("utf-8")) - 1
            selected_student = my_class.students[student_index]

            stdscr.addstr("Enter marks:\n")
            marks = float(stdscr.getstr().decode("utf-8"))
            my_class.add_marks(selected_student.student_id, selected_course.course_id, marks)

        elif key == ord('4'):
            stdscr.clear()
            stdscr.addstr("Calculate GPA\n\n")
            stdscr.addstr("Select a student:\n")