# Left Rotate the Array by One
'''
Given an integer array nums, rotate the array to the left by one.
Note: There is no need to return anything, just modify the given array.
Examples:
Example 1:
Input: nums = [1, 2, 3, 4, 5]  
Output: [2, 3, 4, 5, 1]  
Example 2:
Input:nums = [-1, 0, 3, 6]  
Output:[0, 3, 6, -1]  
'''
class Solution:
    def rotate_left_by_one_place(self, array, size):
        temp = array[0]
        for i in range(1, size):
            array[i - 1] = array[i]
        array[size - 1] = temp

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.rotate_left_by_one_place(array, size)

for i in range(size):
    print(array[i], end = ' ')