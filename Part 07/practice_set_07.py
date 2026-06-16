# Problem 1 -
num = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# Problem 2 -
l = ["Swatika", "Soham", "Sachin", "Rahul"]
for i in l:
    if i.lower().startswith('s'):
        print("Hello", i)

# Problem 3 -
num = int(input("Enter the number: "))
i = 1
while(i <= 10):
    print(f"{num} * {i} = {num * i}")
    i = i + 1

# Problem 4 -
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime number")
else:
    print("Not prime number")

# Problem 5 - 
num = int(input("Enter the number: "))
sum_numbers = 0
i = 1
while(i <= num):
    sum_numbers += i
    i += 1
print(sum_numbers)

# Problem 6 -
num = int(input("Enter the number: "))
fact = 1
if num == 0 or num == 1:
    print(fact)
else:
    for i in range(2, num + 1):
        fact = fact * i 
    print(fact)

# Problem 7 -
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for spaces in range(rows - i):
        print('_', end = ' ')
    for j in range(2 * i - 1):
        print("*", end = ' ')
    print("\n")

# Problem 8 - 
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end = ' ')
    print("\n")

# Problem 9 -
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(i == 1 or i == rows or j == 1 or j == rows):
            print("*", end = ' ')
        else:
            print("_", end = ' ')
    print("\n")

# Problem 10 -
num = int(input("Enter the number: "))
for i in range(10, 0, -1):
    print(f"{num} * {i} = {num * i}")
