import json


# JSON READING
with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

# Calculate the average of grades for each student
def calculate_average(grades):
    total = 0

    for grade in grades:
        total += grade

    average = total / len(grades)
    return average


# Find the student with the highest average
for student in students:
    try:
        average = calculate_average(student["grades"])

        print(student["name"], "-", round(average, 2))

    except ZeroDivisionError:
        print(student["name"], "- no grades")