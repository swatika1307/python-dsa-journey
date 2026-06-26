# Count digits in a number
'''
Problem Statement: Given an integer N, return the number of digits in N.
Examples:
Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.                    
Example 2:
Input:N = 7789              
Output: 4
Explanation: The number 7789 has 4 digits.
'''

from math import log10

# Approach 1:
def count_all_digits1():
    number = int(input("Enter the number: "))
    if number == 0:
        return 1
    count = 0
    while(number > 0):
        last_digit = number % 10 
        count = count + 1
        number = number // 10 
    return count

#Approach 2:
def count_all_digits2():
    number = int(input("Enter the number: "))
    if number == 0:
        return 1
    count = (int)(log10(number) + 1)
    return count

result = count_all_digits1()
print("The number of digits:", result)