# Check if an Array is Sorted
'''
Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.
Examples:
Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.
Example 2:
Input: N = 5, array[] = {5,4,6,7,8}
Output: False.
Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False. Here element 5 is not smaller than or equal to its future elements.
'''
class Solution:
    def check_if_array_is_sorted(self, array, size):
        for i in range(1, size):
            if(array[i] >= array[i - 1]):
                pass
            else:
                return False
        return True
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.check_if_array_is_sorted(array, size)

if result:
    print("Sorted array.")
else:
    print("Not sorted array.")