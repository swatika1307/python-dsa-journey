# Left Rotate array by K elements
'''
Given an array of integers, rotating array of elements by k elements.
Examples:
Input : nums = [1, 2, 3, 4, 5, 6, 7], k = 2
Output : [3, 4, 5, 6, 7, 1, 2]
Input : nums = [1, 2, 3, 4, 5, 6], k = 2
Output : [3, 4, 5, 6, 1, 2]
'''

class Solution:
    # Brute force
    def rotate_left_by_k_places1(self, array, size, k):
        k = k % size
        temp = []
        for i in range(k):
            temp.append(array[i])
        for i in range(k, size):
            array[i - k] = array[i]
        for i in range(k + 1, size):
            array[i] = temp[i - (size - k)]

    # Optimal
    def reverse(self, array, start, end):
        while(start < end):
            array[start], array[end] = array[end], array[start]
            start = start + 1
            end = end - 1

    def rotate_left_by_k_places2(self, array, size, k):
        k = k % size
        self.reverse(array, 0, k - 1)
        self.reverse(array, k, size - 1)
        self.reverse(array, 0, size - 1)

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
k = int(input("Enter the number of places by which you want to left rotate the array: "))

object = Solution()
result = object.rotate_left_by_k_places2(array, size, k)

for i in range(size):
    print(array[i], end = ' ')