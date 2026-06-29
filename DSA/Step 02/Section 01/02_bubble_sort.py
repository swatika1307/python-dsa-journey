# Bubble Sort Algorithm
'''
Given an array of N integers, write a program to implement the Bubble Sorting algorithm.
Examples:
Example 1:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5
Example 2:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52
'''

class Solution:
    def bubble_sort(self, array, size):
        for i in range (size - 1, 0, -1):
            flag = True
            for j in range (0, i):
                if(array[j] > array[j + 1]):
                    flag = False
                    # print("Change")
                    array[j], array[j + 1] = array[j + 1], array[j]
            if flag:
                # print("Sorted")
                break
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
object.bubble_sort(array, size)