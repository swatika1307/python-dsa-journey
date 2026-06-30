# Merge Sort Algorithm
'''
Given an array of size n, sort the array using Merge Sort.
Examples:
Input : N=7,arr[]={3,2,8,5,1,4,23}
Output : {1,2,3,4,5,8,23}
Explanation : Given array is sorted in non-decreasing order.
Input : N=5, arr[]={4,2,1,6,7}
Output : {1,2,4,6,7}
Explanation : Given array is sorted in non-decreasing order.
'''

class Solution:
    def merge(self, array, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        while(left <= mid and right <= high):
            if(array[left] <= array[right]):
                temp.append(array[left])
                left = left + 1
            else:
                temp.append(array[right])
                right = right + 1
        while(left <= mid):
            temp.append(array[left])
            left = left + 1
        while(right <= high):
            temp.append(array[right])
            right = right + 1
        for i in range(low, high + 1):
            array[i] = temp[i - low]

    def mergeSort(self, array, low, high):
        if(low >= high):
            return
        mid = (low + high) // 2
        self.mergeSort(array, low, mid)
        self.mergeSort(array, mid + 1, high)
        self.merge(array, low, mid, high)
        
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
    
object = Solution()
object.mergeSort(array, 0, size - 1)

for i in range(size):
    print(array[i], end = ' ')