# Recursive Bubble Sort Algorithm
'''
Given an array of N integers, write a program to implement the Recursive Bubble Sort algorithm.
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
    def bubble_sort_recursive(self, array, size):
        if size == 1:
            return
        flag = True
        for j in range(size - 1):
            if(array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            return
        self.bubble_sort_recursive(array, size - 1)


array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
object.bubble_sort_recursive(array, size)

for num in array:
    print(num, end = ' ')