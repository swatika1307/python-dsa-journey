# Class creation
class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good morning!")

# Object
swatika = Employee("Swatika", 1400000, "Java")
swatika.greet()
print(swatika.language, swatika.salary)
swatika.getInfo()