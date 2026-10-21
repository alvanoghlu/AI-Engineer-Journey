
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grades: list[int]

    def average(self) -> float:
        if not self.grades:
            raise ValueError("no grades")

        return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
    student1 = Student("Ali", [70, 90])
    student2 = Student("Ali", [70])
    student3 = Student("Ali", [70])

    print(student1)
    print(student2 == student3)
    print("Average:", student1.average())
  