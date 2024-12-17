class Employee : 
    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        print(self.position)

employees = []
employees.append(Employee("John", 30, 20000, "Python Developer"))
employees.append(Employee("Herry", 25, 25000, "Java Developer"))
employees.append(Employee("Zosh", 32, 25500, "React Js"))
employees.append(Employee("Abc", 29, 15000, "Node Js"))

for emp in employees:
    emp.display()
    print("---------")