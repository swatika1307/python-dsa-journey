class Person:
    def __init__(self, name):
        self.name = name
    def showName(self):
        print(f"The name of the person is {self.name}.")

class Age:
    def __init__(self, age):
        self.age = age
    def showAge(self):
        print(f"The age of the person is {self.age}.")

class Employee(Person, Age):
    def __init__(self, name, age, company):
        Person.__init__(self, name)
        Age.__init__(self, age)
        self.company = company
    def showCompany(self):
        print(f"The company name is {self.company}.")

e = Employee("ABC", 23, "XYZ")
e.showName()
e.showAge()
e.showCompany()