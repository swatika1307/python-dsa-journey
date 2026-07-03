# Find missing number
'''
Given an array in which numbers range from 1 to N. Find the missing number.
Examples:
Input: arr[] = [1, 2, 4, 5] N = 5
Output: 3
'''

class Solution:
    def missing_number(self, array, number):
        xor1 = 0
        xor2 = 0
        for i in range(len(array)):
            xor2 = xor2 ^ array[i]
            xor1 = xor1 ^ (i + 1)
        xor1 = xor1 ^ number
        return xor1 ^ xor2
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
number = int(input("Enter the number: "))

object = Solution()
result = object.missing_number(array, number)

print("Missing number:", result)   