
import json

from student import Student
from student_group import StudentGroup


# Read students from JSON
with open("students.json", encoding="utf-8") as f:
    data = json.load(f)


# Create a student group
group = StudentGroup()


# Add students to the group
for d in data:
    student = Student(d["name"], d["grades"])
    group.add(student)


# Print student averages
for student in group.students:
    try:
        print(f"{student.name}: {student.average():.1f}")
    except ValueError:
        print(f"{student.name}: no grades")


# Find the best student using a for loop
best = group.best_student()
print("Best student:", best.name)


# Compare with max() and lambda
valid_students = [
    s for s in group.students if s.grades
]

best_with_max = max(
    valid_students,
    key=lambda s: s.average()
)

print("Best with max:", best_with_max.name)
