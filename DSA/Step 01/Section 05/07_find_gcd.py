# Find GCD of two numbers
'''
Problem Statement: Given two integers N1 and N2, find their greatest common divisor.
Examples
Example 1:
Input: N1 = 9, N2 = 12
Output: 3
Explanation:
Factors of 9: 1, 3, 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3
Greatest common factor: 3 (GCD)
Example 2:
Input: N1 = 20, N2 = 15
Output: 5
Explanation:
Factors of 20: 1, 2, 4, 5, 10, 20
Factors of 15: 1, 3, 5, 15
Common Factors: 1, 5
Greatest common factor: 5 (GCD)
'''
# Approach 1:
def find_gcd1():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    gcd = 1
    for i in range(1, min(number1, number2) + 1):
        if(number1 % i == 0 and number2 % i == 0):
            gcd = i
    return gcd

# Approach 2:
def find_gcd2():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    gcd = 1
    for i in range(min(number1, number2), 0, -1):
        if(number1 % i == 0 and number2 % i == 0):
            gcd = i
            break
    return gcd

# Approach 3:
def find_gcd3():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    while(number1 > 0 and number2 > 0):
        if(number1 > number2):
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    if(number1 == 0):
        return number2
    return number1

result = find_gcd3()
print("GCD is:",result)