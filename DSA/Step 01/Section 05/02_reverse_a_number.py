# Reverse Digits of A Number
'''
Problem Statement: Given an integer N return the reverse of the given number.
Note: If a number has trailing zeros, then its reverse will not include them. For e.g , reverse of 10400 will be 401 instead of 00401.
Examples:
Input: N = 12345
Output:54321
Explanation: The reverse of 12345 is 54321.
Input: N = 7789                
Output: 9877
Explanation: The reverse of number 7789 is 9877.
'''

def reverse_a_number1():
    number = int(input("Enter the number: "))
    reverse_number = 0
    while(number > 0):
        last_digit = number % 10
        reverse_number = (reverse_number * 10) + last_digit
        number = number // 10
    return reverse_number

result = reverse_a_number1()
print("Reverse of the number is:", result)

'''
What if 0 were to be present?
Examples:
Input: N = 10400
Output:00401
'''
def reverse_a_number2():
    number = input("Enter the number: ")
    reverse_number = ""
    for i in range(len(number) - 1, -1, -1):
        reverse_number += number[i]
    return reverse_number

result = reverse_a_number2()
print("Reverse of the number is:", result)