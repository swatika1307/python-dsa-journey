# Find the Largest element in an array
'''
Given an array, we have to find the largest element in the array.
Examples:
Example 1:
Input: arr[] = {2, 5, 1, 3, 0}  
Output: 5  
Explanation: 5 is the largest element in the array.
Example 2:
Input: arr[] = {8, 10, 5, 7, 9}  
Output: 10  
Explanation: 10 is the largest element in the array.
'''

class Solution:
    def largest_element_in_an_array(self, array, size):
        largest = array[0]
        for i in range(1, size):
            if array[i] > largest:
                largest = array[i]
        return largest

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
largestElement = object.largest_element_in_an_array(array, size)

print("The largest element is:", largestElement)