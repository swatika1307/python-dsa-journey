class Employee:
    company = "ABC"
    def showDetails(self):
        print(f"The company is {self.company}.")

class Programmer(Employee):
    company = "XYZ"
    def __init__(self, language):
        self.language = language
    def showLanguage(self):
        print(f"The company is {self.company} and language is {self.language}.")

e = Employee()
p = Programmer("Python")

e.showDetails()
p.showDetails()
p.showLanguage()