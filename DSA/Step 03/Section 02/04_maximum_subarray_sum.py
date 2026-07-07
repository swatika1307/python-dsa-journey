# Kadane's Algorithm : Maximum Subarray Sum in an Array
'''
Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
Examples:
Example 1:
Input: nums = [2, 3, 5, -2, 7, -4]  
Output: 15  
Explanation: The subarray from index 0 to index 4 has the largest sum = 15, which is the maximum sum of any contiguous subarray.
Example 2:
Input: nums = [-2, -3, -7, -2, -10, -4]  
Output: -2  
Explanation: The largest sum is -2, which comes from taking the element at index 0 or index 3 as the subarray. Since all numbers are negative, the subarray with the least negative number gives the largest sum.
'''
class Solution:
    # Brute force
    def maximum_subarray_sum1(self, array, size):
        maxi = float('-inf')
        for i in range(size):
            for j in range(i, size):
                sum = 0
                for k in range(i, j + 1):
                    sum = sum + array[k]
                maxi = max(maxi, sum)
        return maxi
    
    # Better
    def maximum_subarray_sum2(self, array, size):
        maxi = float('-inf')
        for i in range(size):
            sum = 0
            for j in range(i, size):
                sum = sum + array[j]
                maxi = max(maxi, sum)
        return maxi
    
    # Optimal
    def maximum_subarray_sum3(self, array, size):
        sum = 0
        maxi = float('-inf')
        for i in range(size):
            sum = sum + array[i]
            if(sum > maxi):
                maxi = sum
            if(sum < 0):
                sum = 0
        return maxi
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.maximum_subarray_sum3(array, size)

print("Maximum subarray sum:", result)