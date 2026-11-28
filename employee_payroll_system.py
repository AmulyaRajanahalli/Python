class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Payroll(Employee):
    def display(self):
        print("Employee Name:",self.name)
        print("Salary:",self.salary)

name=input("Enter employee name:")
salary=int(input("Enter salary:"))

e=Payroll(name,salary)
e.display()
