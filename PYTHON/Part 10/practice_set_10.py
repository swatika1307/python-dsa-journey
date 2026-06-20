# Problem 1 -
class Programmer:
    company = "Mircrosoft"
    def __init__(self, name, experience, salary):
        self.name = name
        self.experience = experience
        self.salary = salary
    def getInfo(self):
        print(f"Name: {self.name}, Company : {self.company}, Experience: {self.experience}, Salary: {self.salary}.")

programmer_1 = Programmer("Swatika", 5, 1800000)
programmer_2 = Programmer("Bella", 1, 700000)
programmer_1.getInfo()
programmer_2.getInfo()

# Problem 2 -
class Calculator():
    def __init__(self, num):
        self.num = num
    def getSquare(self):
        print(f"The square of the number is {self.num * self.num}.")
    def getCube(self):
        print(f"The cube of the number is {self.num * self.num * self.num}.")
    def getSquareRoot(self):
        print(f"The square root of the number is {self.num ** 1/2}.")

number = Calculator(4)
number.getSquare()
number.getCube()
number.getSquareRoot()

# Problem 3 -
class Example:
    a = 5

object = Example()
print(object.a) # Prints class attribute
object.a = 0
print(object.a) # Prints instance attribute
print(Example.a) # Does not change the class attribute

# Problem 4 -
class Calculator():
    def __init__(self, num):
        self.num = num
    def getSquare(self):
        print(f"The square of the number is {self.num * self.num}.")
    def getCube(self):
        print(f"The cube of the number is {self.num * self.num * self.num}.")
    def getSquareRoot(self):
        print(f"The square root of the number is {self.num ** 1/2}.")
    @staticmethod
    def greet():
        print("Hello User!")

number = Calculator(4)
number.greet()
number.getSquare()
number.getCube()
number.getSquareRoot()

# Problem 5 -
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, source, destination):
        print(f"Train no. {self.trainNo} is running from {source} to {destination}.")
    def getStatus(self):
        print(f"Train no. {self.trainNo} is running on time.")
    def getFare(self, source, destination):
        print(f"The fare of the ticket from {source} to {destination} is {randint(222,555)}.")

travel = Train(12345)
travel.book("Hyderabad", "Bangalore")
travel.getStatus()
travel.getFare("Hyderabad", "Bangalore")

# Problem 6 -
from random import randint
class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    def book(slf, source, destination):
        print(f"Train no. {slf.trainNo} is running from {source} to {destination}.")
    def getStatus(slf):
        print(f"Train no. {slf.trainNo} is running on time.")
    def getFare(slf, source, destination):
        print(f"The fare of the ticket from {source} to {destination} is {randint(222,555)}.")

travel = Train(12345)
travel.book("Hyderabad", "Bangalore")
travel.getStatus()
travel.getFare("Hyderabad", "Bangalore")