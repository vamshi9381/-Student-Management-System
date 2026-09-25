from src.exceptions.student_exceptions import (
    DuplicateStudentException,
    InvalidStudentException,
    StudentNotFoundException
)

from src.models.student import Student

from src.utils.json_handler import JSONHandler

from src.utils.validators import (
    validate_age,
    validate_marks
)


class StudentService:

    def __init__(self):
        self.json_handler = JSONHandler()

    # ==============================
    # ADD STUDENT
    # ==============================

    def add_student(self):

        try:
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            age = int(input("Enter Age: "))
            course = input("Enter Course: ").strip()
            marks = float(input("Enter Marks: "))

            if not student_id or not name or not course:
                raise InvalidStudentException(
                    "Student ID, name, and course are required."
                )

            validate_age(age)
            validate_marks(marks)

            student = Student(
                student_id,
                name,
                age,
                course,
                marks
            )

            self.json_handler.save_student(student)

            print("\nStudent added successfully!")

        except ValueError as exc:
            print(f"\nInvalid input: {exc}")

        except DuplicateStudentException as exc:
            print(f"\n{exc}")

        except InvalidStudentException as exc:
            print(f"\n{exc}")

    # ==============================
    # VIEW STUDENTS
    # ==============================

    def view_students(self):

        students = self.json_handler.get_students()

        if not students:
            print("\nNo students found.")
            return

        print("\n========== STUDENT RECORDS ==========")

        for student in students:
            student.display()

        print("=====================================")

    # ==============================
    # SEARCH STUDENT
    # ==============================

    def search_student(self):

        student_id = input(
            "Enter Student ID to search: "
        ).strip()

        student = self.search_student_by_id(student_id)

        if student is None:
            print("\nStudent not found.")
            return

        print("\nStudent found!")

        student.display()

    def search_student_by_id(self, student_id):

        return self.json_handler.get_student_by_id(student_id)

    # ==============================
    # UPDATE STUDENT
    # ==============================

    def update_student(self):

        student_id = input(
            "Enter Student ID to update: "
        ).strip()

        student = self.search_student_by_id(student_id)

        if student is None:
            print("\nStudent not found.")
            return

        try:

            name = input(
                "Enter new Name "
                "(leave blank to keep current): "
            ).strip()

            if name == "":
                name = student.name

            age_input = input(
                "Enter new Age "
                "(leave blank to keep current): "
            ).strip()

            if age_input == "":
                age = student.age
            else:
                age = int(age_input)

            course = input(
                "Enter new Course "
                "(leave blank to keep current): "
            ).strip()

            if course == "":
                course = student.course

            marks_input = input(
                "Enter new Marks "
                "(leave blank to keep current): "
            ).strip()

            if marks_input == "":
                marks = student.marks
            else:
                marks = float(marks_input)

            validate_age(age)
            validate_marks(marks)

            self.json_handler.update_student(
                student_id,
                name=name,
                age=age,
                course=course,
                marks=marks
            )

            print("\nStudent updated successfully!")

        except ValueError as exc:
            print(f"\nInvalid input: {exc}")

        except StudentNotFoundException as exc:
            print(f"\n{exc}")

    # ==============================
    # DELETE STUDENT
    # ==============================

    def delete_student(self):

        student_id = input(
            "Enter Student ID to delete: "
        ).strip()

        try:

            self.json_handler.delete_student(student_id)

            print("\nStudent deleted successfully!")

        except StudentNotFoundException as exc:

            print(f"\n{exc}")