import json

import pytest

import grades_csv
from grades_csv import DataError, load_grades, parse_row


@pytest.fixture
def sample_csv(tmp_path):
    file = tmp_path / "g.csv"

    file.write_text(
        "name,subject,grade\n"
        "Əli,Math,85\n"
        "Murad,Python,90\n"
        "Aysel,Math,abc\n"
        "Orxan,Python,150\n",
        encoding="utf-8",
    )

    return file


def test_load_grades_skips_bad_rows(sample_csv):
    result = load_grades(sample_csv)

    assert result == [
        {"name": "Əli", "subject": "Math", "grade": 85},
        {"name": "Murad", "subject": "Python", "grade": 90},
    ]


def test_parse_row_valid_grade():
    row = {"name": "Ali", "grade": "85"}

    result = parse_row(row, 2)

    assert result["grade"] == 85
    assert isinstance(result["grade"], int)


import pytest


@pytest.mark.parametrize("bad_grade", ["abc", "150", "-1", ""])
def test_parse_row_rejects_bad_grade(bad_grade):
    row = {"name": "Ali", "subject": "Math", "grade": bad_grade}

    with pytest.raises(DataError):
        parse_row(row, 2)


def test_load_grades_returns_empty_list_for_empty_or_header_only_csv(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("", encoding="utf-8")

    header_file = tmp_path / "header.csv"
    header_file.write_text("name,subject,grade\n", encoding="utf-8")

    assert load_grades(empty_file) == []
    assert load_grades(header_file) == []


def test_main_exports_results_json(tmp_path, monkeypatch):
    csv_file = tmp_path / "grades.csv"
    json_file = tmp_path / "results.json"

    csv_file.write_text(
        "name,subject,grade\nAli,Math,80\nAli,Python,100\nMurad,Math,60\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(grades_csv, "__file__", str(tmp_path / "grades_csv.py"))

    grades_csv.main()

    with json_file.open(encoding="utf-8") as f:
        result = json.load(f)

    assert result == [{"name": "Ali", "average": 90}, {"name": "Murad", "average": 60}]


def test_main_handles_missing_csv_file(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(grades_csv, "__file__", str(tmp_path / "grades_csv.py"))

    grades_csv.main()

    captured = capsys.readouterr()

    assert captured.out.strip() == ("CSV file not found. Please check the file path.")
