# Find next lexicographically greater permutation
'''
Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).
Examples:
Input: Arr[] = {1,3,2}
Output: {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.
Input : Arr[] = {3,2,1}
Output: {1,2,3}
Explanation : As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the lowest permutation.
'''

class Solution:
    def next_permutation(self, array, size):
        idx = -1
        for i in range(size - 2, -1, -1):
            if(array[i] < array[i + 1]):
                idx = i
                break
        if(idx == -1):
            array.reverse()
            return array
        for i in range(size - 1, 0, -1):
            if(array[i] > array[idx]):
                array[i], array[idx] = array[idx], array[i]
                break
        array[(idx + 1):] = array[(idx + 1):][::-1]
        return array

array = []
size = int(input("Enter the size: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.next_permutation(array, size)

for i in range(len(result)):
    print(result[i], end = ' ')