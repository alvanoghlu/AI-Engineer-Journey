import logging
class DataError(Exception):
    pass

def parse_row(row: dict, line_number: int) -> dict:
    try:
        grade = int(row["grade"])
    except ValueError as e:
        raise DataError(
            f"bad grade in row {line_number}: {row['grade']}"
        ) from e

    if not 0 <= grade <= 100:
        raise DataError(
            f"bad grade in row {line_number}: {grade}"
        )

    row["grade"] = grade
    return row


import csv
import json
from pathlib import Path

from grades_utils import calculate_average


# Read and clean CSV data
def load_grades(path: Path) -> list[dict]:
    valid_rows = []
    loaded = 0
    skipped = 0

    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for line_number, row in enumerate(reader, start=2):
            try:
                parsed_row = parse_row(row, line_number)

                valid_rows.append({
                    "name": parsed_row["name"],
                    "subject": parsed_row["subject"],
                    "grade": parsed_row["grade"]
                })

                loaded += 1

            except DataError as e:
                logging.warning(
                    "skipped row %s: %s", line_number, e
                )
                skipped += 1

    print(f"Loaded {loaded} rows, skipped {skipped}")
    logging.info(
        "loaded %s rows, skipped %s",
        loaded,
        skipped
        )
    
    return valid_rows


# Main program
def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        filename="app.log",
        encoding="utf-8",
        format="%(asctime)s %(levelname)s %(message)s"
    )

    # File paths
    folder = Path(__file__).parent
    csv_path = folder / "grades.csv"
    output_path = folder / "results.json"

    # Load CSV data
    try:
        grades = load_grades(csv_path)

    except FileNotFoundError as e:
        logging.error("file not found: %s", e)
        print("CSV file not found. Please check the file path.")

    else:
        # Group grades by student name
        grades_by_name = {}

        for student in grades:
            name = student["name"]
            grade = student["grade"]

            if name not in grades_by_name:
                grades_by_name[name] = []

            grades_by_name[name].append(grade)

        # Calculate average grades
        result = []

        for name, student_grades in grades_by_name.items():
            average = calculate_average(student_grades)

            result.append({
                "name": name,
                "average": average
            })

        # Export results to JSON
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(
                result,
                f,
                indent=2,
                ensure_ascii=False
            )

        print("Results exported successfully!")

if __name__ == "__main__":
    main()