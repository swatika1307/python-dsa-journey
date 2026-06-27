# Sum of first N Natural Numbers
'''
Given a number ‘N’, find out the sum of the first N natural numbers .
Examples:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=21
'''

def sum_of_n_numbers(n):
    if (n == 0):
        return 0
    return n + sum_of_n_numbers(n - 1)

number = int(input("Enter the value of n: "))
result = sum_of_n_numbers(number)
print(result)