
import csv
from pathlib import Path


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



if __name__ == "__main__":
    csv_path = Path(__file__).parent / "grades.csv"

    grades = load_grades(csv_path)

    for student in grades:
        print(student)
