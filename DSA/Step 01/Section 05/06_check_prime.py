# Check if a number is prime or not
'''
Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.
Examples:
Example 1:
Input:N = 2          
Output:True          
Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).                                 
Example 2:
Input:N =10                              
Output: False              
Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.
'''
import math
# Approach 1:
def check_prime1():
    number = int(input("Enter the number: "))
    count = 0
    for i in range(1, number + 1):
        if(number % i == 0):
            count = count + 1
    if(count == 2):
        return True
    return False

# Approach 2:
def check_prime2():
    number = int(input("Enter the number: "))
    count = 0
    for i in range(1, int(math.sqrt(number) + 1)):
        if(number % i == 0):
            count = count + 1
            if((number // i) != i):
                count = count + 1
    if(count == 2):
        return True
    return False

result = check_prime2()
if result:
    print("Prime Number")
else:
    print("Not Prime Number")