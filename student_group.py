
from student import Student


class StudentGroup:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def add(self, student: Student) -> None:
        self.students.append(student)

    def best_student(self) -> Student:
        if not self.students:
            raise ValueError("group is empty")

        best: Student | None = None

        for student in self.students:
            # Design decision:
            # Skip students who have no grades.
            if not student.grades:
                continue

            if best is None or student.average() > best.average():
                best = student

        if best is None:
            raise ValueError("no students with grades")

        return best
  