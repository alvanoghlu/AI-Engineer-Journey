
import csv
import json
from pathlib import Path

from grades_utils import calculate_average


# Read and clean CSV data
def load_grades(path: Path) -> list[dict]:
    valid_rows = []
    skipped = 0

    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                grade = int(row["grade"])

            except ValueError:
                skipped += 1
                continue

            if not 0 <= grade <= 100:
                skipped += 1
                continue

            valid_rows.append({
                "name": row["name"],
                "subject": row["subject"],
                "grade": grade
            })

    print(f"Skipped {skipped} rows")
    return valid_rows


# Main program
if __name__ == "__main__":

    # File paths
    folder = Path(__file__).parent
    csv_path = folder / "grades.csv"
    output_path = folder / "results.json"

    # Load CSV data
    try:
        grades = load_grades(csv_path)

    except FileNotFoundError:
        print("CSV file not found!")

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
