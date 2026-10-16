grades = [70, 85, 90, 65, 95, 80]
def find_highest_grade(grades):
    highest_grade = grades[0]
    for grade in grades:
        if grade > highest_grade:
            highest_grade = grade
    return highest_grade

result = find_highest_grade(grades)

print("The highest grades is:", result)

