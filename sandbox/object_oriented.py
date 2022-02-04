"""Messing around with objects and classes."""

suite: dict[str, str] = {
    "710A1": "John Tevez",
    "710A2": "Connor Downing",
    "710B1": "Anthony Valentino",
    "710B2": "Charles Armstrong",
    "710C1": "Evan Hernandez",
    "710C2": "Tanner Bentley",
    "710D1": "Walker Franklin",
    "710D2": "Nathan Adams"
}


class Tarheel:
    name: str = ""
    PID: int = 0
    year: str = ""

    def __init__(self, student_name: str, student_PID: int, student_year: str):
        self.name = student_name
        self.PID = student_PID
        self.year = student_year


student1: Tarheel = Tarheel("Anthony Valentino", 730466997, "Freshman")

print(student1.name)
print(student1.PID)
print(student1.year)