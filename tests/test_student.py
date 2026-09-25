import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from models.student import Student
from services.student_service import StudentService


def test_add_and_view_student(tmp_path, monkeypatch):
    service = StudentService()
    service.file_handler.FILE_PATH = tmp_path / "students.txt"

    answers = iter(["S001", "Alice", "20", "Python", "95.5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    service.add_student()

    students = service.file_handler.get_students()
    assert len(students) == 1
    assert students[0].student_id == "S001"
    assert students[0].name == "Alice"
    assert students[0].age == 20
    assert students[0].course == "Python"
    assert students[0].marks == 95.5


def test_search_update_and_delete_student(tmp_path):
    service = StudentService()
    service.file_handler.FILE_PATH = tmp_path / "students.txt"

    service.file_handler.save_student(Student("S002", "Bob", 22, "Java", 88.0))

    found = service.search_student_by_id("S002")
    assert found is not None
    assert found.name == "Bob"

    service.update_student_by_id("S002", name="Bobby", age=23, course="Data Science", marks=92.5)
    updated = service.search_student_by_id("S002")
    assert updated.name == "Bobby"
    assert updated.age == 23
    assert updated.course == "Data Science"
    assert updated.marks == 92.5

    service.delete_student_by_id("S002")
    assert service.search_student_by_id("S002") is None
