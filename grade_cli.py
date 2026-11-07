import argparse
import sys
from pathlib import Path

from grades_csv import load_grades
from grades_utils import calculate_average


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze student grades from a CSV file"
    )

    parser.add_argument(
        "command",
        choices=["average", "top", "summary"],
        help="Choose the operation to run",
    )

    parser.add_argument(
        "--file",
        default=Path(__file__).parent / "grades.csv",
        help="Path to the grades CSV file",
    )

    return parser

def group_by_name(
    rows: list[dict[str, str | int]],
) -> dict[str, list[int]]:
    grades_by_name = {}

    for row in rows:
        name = row["name"]
        grade = row["grade"]

        if name not in grades_by_name:
            grades_by_name[name] = []

        grades_by_name[name].append(grade)

    return grades_by_name


def show_average(rows: list[dict[str, str | int]]) -> None:
    grades_by_name = group_by_name(rows)

    for name, grades in grades_by_name.items():
        average = calculate_average(grades)
        print(f"{name}: {average}")


def show_top(rows: list[dict[str, str | int]]) -> None:
    grades_by_name = group_by_name(rows)

    if not grades_by_name:
        print("No student data found")
        return

    averages = {}

    for name, grades in grades_by_name.items():
        averages[name] = calculate_average(grades)

    top_student = max(averages, key=averages.get)

    print(f"Top student: {top_student}")
    print(f"Average grade: {averages[top_student]}")


def show_summary(rows: list[dict[str, str | int]]) -> None:
    grades_by_name = group_by_name(rows)

    if not rows:
        print("No student data found")
        return

    all_grades = [row["grade"] for row in rows]

    overall_average = calculate_average(all_grades)

    print(f"Total students: {len(grades_by_name)}")
    print(f"Total grades: {len(rows)}")
    print(f"Overall average: {overall_average}")


def main() -> None:
    args = build_parser().parse_args()

    csv_path = Path(args.file)

    try:
        rows = load_grades(csv_path)

    except FileNotFoundError:
        print("CSV file not found")
        sys.exit(1)

    if args.command == "average":
        show_average(rows)

    elif args.command == "top":
        show_top(rows)

    elif args.command == "summary":
        show_summary(rows)


if __name__ == "__main__":
    main()
