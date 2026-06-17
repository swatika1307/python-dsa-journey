age = int(input("Enter your age: "))
if age >= 18:
    print("Yes")
else:
    print("No")
print("End of program")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are above the age of consent")
elif age < 0:
    print("Age cannot be negative")
elif age == 0:
    print("Age cannot be 0")
else:
    print("You are below the age of consent")
print("End of program")