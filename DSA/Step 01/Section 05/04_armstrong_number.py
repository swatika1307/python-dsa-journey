# Check if a number is Armstrong Number or not
'''
Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.
An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
Examples:
Example 1:
Input:N = 153
Output:True
Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153                                      
Example 2:
Input:N = 371                
Output: True
Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371
'''

def armstrong_number():
    number = int(input("Enter the number: "))
    temp = number
    armstrong_number = 0
    while(number > 0):
        last_digit = number % 10
        armstrong_number = armstrong_number + (last_digit * last_digit * last_digit)
        number = number // 10
    if(temp == armstrong_number):
        return True
    return False

result = armstrong_number()
if result:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")