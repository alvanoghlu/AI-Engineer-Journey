grades = [70,85,90]
total = 0
for grade in grades:
    total += grade
average = float(total / len(grades))

print("Average grade:", round(average,2))