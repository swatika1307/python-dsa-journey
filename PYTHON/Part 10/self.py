# Class creation
class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good morning!")

# Object
swatika = Employee()
print(swatika.language, swatika.salary)
swatika.greet()
swatika.getInfo()
Employee.getInfo(swatika)