# Recursive Insertion Sort Algorithm
'''
Given an array of N integers, write a program to implement the Recursive Insertion Sort algorithm.
Examples:
Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52
Example 2:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5
'''

class Solution:
    def insertion_sort_recursive(self, array, i, size):
        if i == size:
            return
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        self.insertion_sort_recursive(array, i + 1, size)

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
object.insertion_sort_recursive(array, 0, size)

for num in array:
    print(num, end = ' ')