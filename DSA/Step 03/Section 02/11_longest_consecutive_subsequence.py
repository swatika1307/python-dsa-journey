# Longest Consecutive Sequence in an Array
'''
Given an array nums of n integers. Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.
Examples:
Example 1:
Input:nums = [100, 4, 200, 1, 3, 2]  
Output: 4  
Explanation: The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.
Example 2:
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  
Output: 9  
Explanation: The longest sequence of consecutive elements in the array is [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9.
'''

class Solution:
    # Brute force
    def linear_search(self, array, num):
        for i in range(len(array)):
            if(array[i] == num):
                return True
        return False
    
    def longest_consecutive_subsequence1(self, array, size):
        longest = 1
        for i in range(size):
            x = array[i]
            cnt = 1
            while(self.linear_search(array, x + 1) == True):
                x = x + 1
                cnt = cnt + 1
            longest = max(longest, cnt)
        return longest
    
    # Better
    def longest_consecutive_subsequence2(self, array, size):
        if size == 0:
            return 0
        array.sort()
        longest = 1
        current_cnt = 0
        lastSmallest = float('-inf')
        for i in range(size):
            if(array[i] - 1 == lastSmallest):
                current_cnt = current_cnt + 1
                lastSmallest = array[i]
            elif(array[i] != lastSmallest):
                current_cnt = 1
                lastSmallest = array[i]
            longest = max(longest, current_cnt)
        return longest
    
    # Optimal
    def longest_consecutive_subsequence3(self, array, size):
        if size == 0:
            return 0
        s = set()
        longest = 1
        for i in range(size):
            s.add(array[i])
        for i in s:
            if i - 1 not in s:
                cnt = 1
                x = i
            while(x + 1 in s):
                x = x + 1
                cnt = cnt + 1
            longest = max(longest, cnt)
        return longest

array = []
size = int(input("Enter the size: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.longest_consecutive_subsequence3(array, size)

print("Length:", result)