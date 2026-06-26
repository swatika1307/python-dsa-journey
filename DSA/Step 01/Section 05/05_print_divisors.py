# Print all Divisors of a given Number
'''
Problem Statement: Given an integer N, return all divisors of N.
A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.
Examples:
Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
Input: N = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.
'''
import math

# Approach 1:
def print_divisors1():
    number = int(input("Enter the number: "))
    for i in range(1, number + 1):
        if(number % i == 0):
            print(i, end = ' ')
    print()

# Approach 2:
def print_divisors2():
    number = int(input("Enter the number: "))
    result = []
    for i in range(1, int(math.sqrt(number) + 1)):
        if(number % i == 0):
            result.append(i)
            if((number // i) != i):
                result.append(number // i)
    result.sort()
    for i in result:
        print(i, end = ' ')
    print()

result = print_divisors2()