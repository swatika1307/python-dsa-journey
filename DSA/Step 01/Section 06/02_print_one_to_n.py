# Print 1 to N using Recursion
'''
Given an integer N, write a program to print numbers from 1 to N.
Examples:
Input: N = 4
Output: 1, 2, 3, 4
Explanation: All the numbers from 1 to 4 are printed.
Input: N = 1
Output: 1 
Explanation: This is the base case.
'''

def print_one_to_n(i, n):
    if(i > n):
        return
    print(i)
    print_one_to_n(i + 1, n)

number = int(input("Enter number till which you want to print the series: "))
i = 1
print_one_to_n(i, number)