
import json
import pytest

from student import Student
from student_group import StudentGroup


def test_best_student():
    group = StudentGroup()

    with open("students.json", encoding="utf-8") as f:
        data = json.load(f)

    for d in data:
        group.add(Student(d["name"], d["grades"]))

    assert group.best_student().name == "Aysel"


def test_empty_group():
    group = StudentGroup()

    with pytest.raises(ValueError, match="group is empty"):
        group.best_student()


def test_student_without_grades():
    group = StudentGroup()

    group.add(Student("Leyla", []))
    group.add(Student("Ali", [70, 85, 90]))

    assert group.best_student().name == "Ali"
