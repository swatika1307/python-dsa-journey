# Problem 1 -
class TwoDVector:
    def __init__(self, i, j):
        self.i = i 
        self.j = j
    def show(self):
        print(f"Vector: {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"Vector: {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(1, 2, 3)
b.show()

# Problem 2 -
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Barking!")

d = Dog()
d.bark()