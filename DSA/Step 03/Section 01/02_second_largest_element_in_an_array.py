# Find Second Largest Element in an array
'''
Given an array, find the second largest element in the array. Print -1 in the event that either of them does not exist.
Examples:
Example 1:
Input: [1, 2, 4, 7, 7, 5]  
Output: Second Largest : 5  
Example 2:
Input: [1]  
Output: -1
'''
class Solution:
    def second_largest_element_in_an_array(self, array, size):
        if size < 2:
            return -1
        largest = array[0]
        secondLargest = float('-inf')
        for i in range(size):
            if(array[i] > largest):
                secondLargest = largest
                largest = array[i]
            elif(array[i] < largest and array[i] > secondLargest):
                secondLargest = array[i]
        return secondLargest
   
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
secondLargestElement = object.second_largest_element_in_an_array(array, size)

if secondLargestElement == -1:
    print("Second largest element is:", secondLargestElement)
else:
    print("Second largest element is:", secondLargestElement)