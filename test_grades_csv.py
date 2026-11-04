import pytest
from grades_csv import parse_row, DataError


def test_parse_row_valid_grade():
    row = {"name": "Ali", "grade": "85"}

    result = parse_row(row, 2)

    assert result["grade"] == 85
    assert isinstance(result["grade"], int)


def test_parse_row_invalid_grade():
    row = {"name": "Ali", "grade": "abc"}

    with pytest.raises(DataError):
        parse_row(row, 2)


def test_parse_row_grade_out_of_range():
    row = {"name": "Ali", "grade": "150"}

    with pytest.raises(DataError):
        parse_row(row, 2)