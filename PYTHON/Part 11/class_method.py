class Demo:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}.")

obj = Demo()
obj.a = 45
obj.show()