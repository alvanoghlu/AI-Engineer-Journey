import pytest

from student import Student
from student_group import StudentGroup


def test_best_student():
    group = StudentGroup()

    students = [
        Student("Aysel", [90, 95, 100]),
        Student("Ali", [70, 80, 85]),
        Student("Leyla", [60, 75, 80]),
    ]

    for student in students:
        group.add(student)

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
