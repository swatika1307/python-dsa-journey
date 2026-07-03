# Linear Search
'''
Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
Examples:
Example 1:
Input: arr[] = 1 2 3 4 5, num = 3  
Output: 2  `
Example 2:
Input: arr[] = 5 4 3 2 1, num = 5  
Output: 0  
 '''

class Solution:
    def linear_search(self, array, size, target):
        for i in range(size):
            if(array[i] == target):
                return i
        return -1
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
target = int(input("Enter the number to be searched: "))

object = Solution()
result = object.linear_search(array, size, target)

if(result == -1):
    print("The number is not present")
else:
    print("The number occurs at index:", result)