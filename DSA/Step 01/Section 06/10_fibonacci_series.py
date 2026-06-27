# Print Fibonacci Series up to Nth term
'''
Given an integer N. Print the Fibonacci series Nth term.
Examples:
Example 1:
Input: N = 5
Output: 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)
Example 2:
Input: 6
Output: 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)
'''

class Solution:
    def fibonacci_series(self, n):
        if(n <= 1):
            return n
        return self.fibonacci_series(n - 1) + self.fibonacci_series(n - 2)

number = int(input("Enter the number of terms you want: "))  
object = Solution()
result = object.fibonacci_series(number)
print(result)