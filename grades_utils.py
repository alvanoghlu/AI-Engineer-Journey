
def calculate_average(grades: list[int]) -> float:
    # In empty list, raise a ValueError
    if len(grades) == 0:
        raise ValueError("Grades list cannot be empty")

    total = 0

    for grade in grades:
        total += grade

    return total / len(grades)

def find_highest_grade(grades: list[int]) -> int:
    # In empty list, raise a ValueError
    if len(grades) == 0:
        raise ValueError("Grades list cannot be empty")

    highest_grade = grades[0]

    for grade in grades:
        if grade > highest_grade:
            highest_grade = grade

    return highest_grade
