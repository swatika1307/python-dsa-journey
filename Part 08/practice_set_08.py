'''
# Problem 1 -
def greatestOfThreeNumbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    return num3
result = greatestOfThreeNumbers()
print(result)

# Problem 2 -
def celsiusToFahrenheit(temperature):
    answer = (temperature * 1.8) + 32
    return answer
temperature = float(input("Enter the temperature: "))
result = celsiusToFahrenheit(temperature)
print(result)

# Problem 3 - 
# end = '' 

# Problem 4 -
def sumOfNauralNumbers(number):
    if number == 1:
        return 1
    return number + sumOfNauralNumbers(number - 1)
number = int(input("Enter the number : "))
result = sumOfNauralNumbers(number)
print(result)

# Problem 5 -
def patternStar(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i + 1):
            print("*", end = ' ')
        print("\n")
rows = int(input("Enter the number of rows: "))
patternStar(rows)

# Problem 6 -
def inchesToCentimeters(length):
    answer = length * 2.54
    return answer
length = float(input("Enter the length: "))
result = inchesToCentimeters(length)
print(result)'''

# Problem 7 -
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["Swatika", "Apple", "Watch", "And", "An"]
print(rem(l, "An"))

# Problem 8 -
def multiplication(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
number = int(input("Enter the number: "))
multiplication(number)