# Find the number that appears once, and the other numbers twice
'''
Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
Examples:
Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
'''
class Solution:
    def appearing_once(self, array, size):
        result = 0
        for i in range(size):
            result = result ^ array[i]
        return result

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.appearing_once(array, size)

print(result)   