class Employee:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}({self.age}, {self.gender})"

emp1 = Employee("John", 23, "Male")
emp2 = Employee("Herry", 24, "female")
emp3 = Employee("jeel", 30, "male")

print(emp1)
print(emp2)
print(emp3)
