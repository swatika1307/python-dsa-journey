# Insertion Sort Algorithm
'''
Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
Examples:
Example 1:
Input:
nums = [7, 4, 1, 5, 3]  
Output: [1, 3, 4, 5, 7]  
Explanation: The array is sorted in non-decreasing order: 1 ≤ 3 ≤ 4 ≤ 5 ≤ 7.
Example 2:
Input:nums = [5, 4, 4, 1, 1]  
Output:[1, 1, 4, 4, 5]  
Explanation: The array is sorted in non-decreasing order: 1 ≤ 1 ≤ 4 ≤ 4 ≤ 5.
'''

class Solution:
    def insertion_sort(self, array, size):
        for i in range(size):
            j = i
            while(j > 0 and array[j - 1] > array[j]):
                array[j - 1], array[j] = array[j], array[j - 1]
                j = j - 1
        print("Sorted array in ascending order is: ")
        for num in array:
            print(num, end = ' ')
        print()

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
object.insertion_sort(array, size)