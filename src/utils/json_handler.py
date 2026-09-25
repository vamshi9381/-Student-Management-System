import json
import os

from src.models.student import Student

from src.exceptions.student_exceptions import (
    DuplicateStudentException,
    StudentNotFoundException
)


class JSONHandler:

    FILE_PATH = "data/students.json"

    def save_student(self, student):

        students = self.get_students()

        for existing_student in students:

            if existing_student.student_id == student.student_id:
                raise DuplicateStudentException(
                    "Student ID already exists."
                )

        students.append(student)

        self._write_students(students)

    def get_students(self):

        if not os.path.exists(self.FILE_PATH):
            return []

        try:

            with open(self.FILE_PATH, "r") as file:
                data = json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            return []

        students = []

        for item in data:

            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
            )

            students.append(student)

        return students

    def get_student_by_id(self, student_id):

        students = self.get_students()

        for student in students:

            if student.student_id == student_id:
                return student

        return None

    def update_student(self, student_id, **updates):

        students = self.get_students()

        found = False

        for student in students:

            if student.student_id == student_id:

                for key, value in updates.items():
                    setattr(student, key, value)

                found = True
                break

        if not found:
            raise StudentNotFoundException(
                "Student not found."
            )

        self._write_students(students)

        return self.get_student_by_id(student_id)

    def delete_student(self, student_id):

        students = self.get_students()

        new_students = []

        deleted = False

        for student in students:

            if student.student_id == student_id:
                deleted = True
            else:
                new_students.append(student)

        if not deleted:
            raise StudentNotFoundException(
                "Student not found."
            )

        self._write_students(new_students)

        return True

    def _write_students(self, students):

        data = []

        for student in students:

            data.append({
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "marks": student.marks
            })

        os.makedirs("data", exist_ok=True)

        with open(self.FILE_PATH, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )