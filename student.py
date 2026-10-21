
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if not self.grades:
            raise ValueError("no grades")

        total = 0
        for grade in self.grades:
            total += grade

        return total / len(self.grades)


ali = Student("Ali", [70, 85, 90])
leyla = Student("Leyla", [90, 95, 100])
murad = Student("Murad", [60, 70, 80])

print(ali.name, ali.average())
print(leyla.name, leyla.average())
print(murad.name, murad.average())
