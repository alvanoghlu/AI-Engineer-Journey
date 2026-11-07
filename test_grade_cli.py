from grade_cli import build_parser, group_by_name


def test_group_by_name() -> None:
    rows = [
        {"name": "Ali", "grade": 80},
        {"name": "Ali", "grade": 90},
        {"name": "Murad", "grade": 70},
    ]

    result = group_by_name(rows)

    assert result == {"Ali": [80, 90], "Murad": [70]}


def test_build_parser() -> None:
    args = build_parser().parse_args(["average", "--file", "x.csv"])

    assert args.command == "average"
    assert args.file == "x.csv"
