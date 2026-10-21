
import pytest
from student import Student


def test_average_normal():
    student = Student("Ali", [70, 90])
    assert student.average() == 80


def test_average_empty():
    student = Student("Ali", [])

    with pytest.raises(ValueError):
        student.average()
