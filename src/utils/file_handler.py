from pathlib import Path

from exceptions.student_exceptions import DuplicateStudentException, StudentNotFoundException
from models.student import Student


class FileHandler:

    FILE_PATH = Path(__file__).resolve().parents[2] / "data" / "students.txt"

    def __init__(self, file_path=None):
        if file_path is not None:
            self.FILE_PATH = Path(file_path)
        self.FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    def _write_students(self, students):
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            for student in students:
                file.write(
                    f"{student.student_id},"
                    f"{student.name},"
                    f"{student.age},"
                    f"{student.course},"
                    f"{student.marks}\n"
                )

    def save_student(self, student):
        students = self.get_students()
        if any(existing.student_id == student.student_id for existing in students):
            raise DuplicateStudentException("Student ID already exists.")

        students.append(student)
        self._write_students(students)

    def get_students(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                lines = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            return []

        students = []
        for line in lines:
            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 5:
                continue
            try:
                students.append(Student(parts[0], parts[1], parts[2], parts[3], parts[4]))
            except (TypeError, ValueError):
                continue
        return students

    def get_student_by_id(self, student_id):
        for student in self.get_students():
            if student.student_id == str(student_id).strip():
                return student
        return None

    def update_student(self, student_id, **updates):
        students = self.get_students()
        for index, student in enumerate(students):
            if student.student_id == str(student_id).strip():
                for key, value in updates.items():
                    if value is None:
                        continue
                    setattr(student, key, value)
                self._write_students(students)
                return student
        raise StudentNotFoundException("Student not found.")

    def delete_student(self, student_id):
        students = self.get_students()
        filtered = [student for student in students if student.student_id != str(student_id).strip()]
        if len(filtered) == len(students):
            raise StudentNotFoundException("Student not found.")
        self._write_students(filtered)
        return True