# Count Maximum Consecutive One's in the array
'''
Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..
Examples:
Example 1:
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Example 2:
Input: prices = {1, 0, 1, 1, 0, 1} 
Output: 2
'''           

class Solution:
    def maximum_consecutive_ones(self, array, size):
        maxi = 0
        count = 0
        for i in range(size):
            if(array[i] == 1):
                count = count + 1
                maxi = max(maxi, count)
            else:
                count = 0
        return maxi

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.maximum_consecutive_ones(array, size)

print(result)   