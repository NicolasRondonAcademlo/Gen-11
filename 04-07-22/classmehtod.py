from datetime import date
from mimetypes import init

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        return f"La edad de {name} es {date.today().year - birth_year} "

    def show(self):
        return f"La edad de {self.name} es {self.age}"

joy = Student.calculate_age("Joy", 1995)
print(joy)


