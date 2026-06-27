# Given an integer N, write a program to print your name N times.
'''
Examples
Input: N = 3
Output: Ashish Ashish Ashish 
Explanation: Name is printed 3 times.
Input: N = 1
Output: Ashish 
Explanation: Name is printed once.
'''

def print_name(i, n):
    if(i > n):
        return
    print("Swatika")
    print_name(i + 1, n)


number = int(input("Enter the number of times you want the name to be printed: "))
i = 1
print_name(i, number)