#!/usr/bin/python3

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = last + '.' + first + '@company.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp1 = Employee("Abel", "mesfin")
emp2 = Employee("metadel", "asmamaw")

print(emp1.fullname())
print(Employee.fullname(emp2))
print(emp2.email)

