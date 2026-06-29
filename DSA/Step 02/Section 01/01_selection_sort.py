# Selection Sort Algorithm
'''
Given an array of N integers, write a program to implement the Selection sorting algorithm.
Examples:
Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52
Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5
'''

class Solution:
    def selection_sort(self, array, size):
        for i in range(size - 1):
            mini = i
            # print("Mini assumed:", array[i])
            for j in range(i, size):
                if(array[j] < array[mini]):
                    mini = j
            # print("Minimum:", array[j])
            temp = array[i]
            array[i] = array[mini]
            array[mini] = temp
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
object.selection_sort(array, size)