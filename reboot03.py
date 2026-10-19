
students = [
    {"name": "Ali", "grades": [70, 85, 90]},
    {"name": "Aysel", "grades": [90, 95, 100]},
    {"name": "Murad", "grades": [80, 75, 85]}
]


def calculate_average(grades):
    total = 0

    for grade in grades:
        total += grade

    average = total / len(grades)
    return average


highest_student = students[0]["name"]
highest_average = calculate_average(students[0]["grades"])

for student in students:
    average = calculate_average(student["grades"])

    print(student["name"], "-", round(average, 2))

    if average > highest_average:
        highest_average = average
        highest_student = student["name"]


print("Highest average student:", highest_student)
print("Highest average:", round(highest_average, 2))