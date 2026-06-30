# Quick Sort Algorithm
'''
Given an array of n integers, sort the array using the Quicksort method.
Examples
Input: N = 5, Arr[] = {4,1,7,9,3}
Output: {1, 3, 4, 7, 9}
Explanation: After sorting the array in ascending order it becomes 1, 3, 4, 7, 9
Input: N = 8, Arr[] = {4,6,2,5,7,9,1,3}
Output: {1, 2, 3, 4, 5, 6, 7, 9}
Explanation: After sorting the array in ascending order it becomes 1, 2, 3, 4, 5, 6, 7, 9
'''

class Solution:
    def quick_sort(self, array, low, high):
        if(low < high):
            partitionIndex = self.partition(array, low, high)
            self.quick_sort(array, low, partitionIndex - 1)
            self.quick_sort(array, partitionIndex + 1, high)
    
    def partition(self, array, low, high):
        pivot = array[low]
        i = low
        j = high
        while(i < j):
            while(array[i] <= pivot and i <= high - 1):
                i = i + 1
            while(array[j] > pivot and j >= low + 1):
                j = j - 1
            if(i < j):
                array[i], array[j] = array[j], array[i]
        array[j], array[low] = array[low], array[j]
        return j        

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
    
object = Solution()
object.quick_sort(array, 0, size - 1)

for i in range(size):
    print(array[i], end = ' ')