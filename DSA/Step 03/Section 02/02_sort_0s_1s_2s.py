# Sort an array of 0s, 1s and 2s
'''
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
Examples:
Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two
Input: nums = [0, 0, 1, 1, 1]
Output: [0, 0, 1, 1, 1]
Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos.
'''

class Solution:
    # Brute force
    def sort_0s_1s_2s1(self, array, size):
        array.sort()
        return array

    # Better
    def sort_0s_1s_2s2(self, array, size):
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(size):
            if(array[i] == 0):
                cnt0 = cnt0 + 1
            elif(array[i] == 1):
                cnt1 = cnt1 + 1
            else:
                cnt2 = cnt2 + 1
        for i in range(cnt0):
            array[i] = 0
        for i in range(cnt0, cnt0 + cnt1):
            array[i]= 1
        for i in range(cnt0 + cnt1, size):
            array[i] = 2
        return array
    
    # Optimal
    def sort_0s_1s_2s3(self, array, size):
        low = 0
        mid = 0
        high = size - 1
        while(mid <= high):
            if array[mid] == 0:
                array[low], array[mid] = array[mid], array[low]
                low = low + 1
                mid = mid + 1
            elif array[mid] == 1:
                mid = mid + 1
            else:
                array[mid], array[high] = array[high], array[mid]
                high = high - 1
        return array
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.sort_0s_1s_2s3(array, size)

for i in range(len(result)):
    print(result[i], end = ' ')