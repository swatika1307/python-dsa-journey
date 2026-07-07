# Find the Majority Element that occurs more than N/2 times
'''
Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.
Examples
Example 1:
Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
Output: 7  
Explanation: The number 7 appears 5 times in the 9-sized array, making it the most frequent element.
Example 2:
Input: nums = [1, 1, 1, 2, 1, 2]  
Output: 1  
Explanation: The number 1 appears 4 times in the 6-sized array, making it the most frequent element.
'''

class Solution:
    # Brute force
    def majority_element1(self, array, size):
        for i in range(size):
            cnt = 0
            for j in range(size):
                if(array[i] == array[j]):
                    cnt = cnt + 1
            if(cnt > size //2):
                return array[i]
        return -1
    
    # Better
    def majority_element2(self, array, size):
        hashMap = {}
        for i in range(size):
            hashMap[array[i]] = hashMap.get(array[i], 0) + 1
        for i in hashMap:
            if(hashMap[i] > size // 2):
                return i
        return -1
    
    # Optimal
    def majority_element3(self, array, size):
        cnt = 0
        ele = 0
        for i in range(size):
            if cnt == 0:
                cnt = 1
                ele = array[i]
            elif array[i] == ele:
                cnt = cnt + 1
            else:
                cnt = cnt - 1
        counter = 0
        for i in range(size):
            if array[i] == ele:
                counter = counter + 1
        if counter > size // 2:
            return ele
        return -1
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.majority_element3(array, size)

print("Majority element:", result)