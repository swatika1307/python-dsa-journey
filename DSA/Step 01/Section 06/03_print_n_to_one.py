# Print N to 1 using Recursion
'''
Given an integer N, write a program to print numbers from N to 1.
Examples:
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.
Input: N = 1
Output: 1 
Explanation: This is the base case.
'''

def print_n_to_one(n, i):
    if(n < i):
        return
    print(n)
    print_n_to_one(n - 1, i)

number = int(input("Enter the number till which you want to print the series: "))
i = 1
print_n_to_one(number, i)