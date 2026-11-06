import pytest
from grades_csv import parse_row, DataError
import pytest
from grades_csv import load_grades


@pytest.fixture
def sample_csv(tmp_path):
    file = tmp_path / "g.csv"

    file.write_text(
        "name,subject,grade\n"
        "Əli,Math,85\n"
        "Murad,Python,90\n"
        "Aysel,Math,abc\n"
        "Orxan,Python,150\n",
        encoding="utf-8"
    )

    return file

def test_load_grades_skips_bad_rows(sample_csv):
    result = load_grades(sample_csv)

    assert result == [
        {"name": "Əli", "subject": "Math", "grade": 85},
        {"name": "Murad", "subject": "Python", "grade": 90}
    ]


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

def test_load_grades_returns_empty_list_for_empty_or_header_only_csv(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("", encoding="utf-8")

    header_file = tmp_path / "header.csv"
    header_file.write_text(
        "name,subject,grade\n",
        encoding="utf-8"
    )

    assert load_grades(empty_file) == []
    assert load_grades(header_file) == []