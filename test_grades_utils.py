
import pytest

from grades_utils import calculate_average, find_highest_grade


# 1. Normal list
def test_average_normal():
    result = calculate_average([70, 85, 90])
    assert result == pytest.approx(81.67, abs=0.01)


def test_highest_normal():
    result = find_highest_grade([70, 85, 90])
    assert result == 90


# 2. Single element list
def test_average_single():
    assert calculate_average([92]) == 92


def test_highest_single():
    assert find_highest_grade([92]) == 92


# 3. Negative numbers
def test_average_negative():
    result = calculate_average([-5, -3, -8])
    assert result == pytest.approx(-5.33, abs=0.01)


def test_highest_negative():
    assert find_highest_grade([-5, -3, -8]) == -3


# 4. Empty list
def test_average_empty():
    with pytest.raises(ValueError):
        calculate_average([])


def test_highest_empty():
    with pytest.raises(ValueError):
        find_highest_grade([])


# 5. All elements are the same
def test_average_equal():
    assert calculate_average([80, 80, 80]) == 80


def test_highest_equal():
    assert find_highest_grade([80, 80, 80]) == 80

def test_highest_normal():
    result = find_highest_grade([70, 85, 90])
    assert result == 90