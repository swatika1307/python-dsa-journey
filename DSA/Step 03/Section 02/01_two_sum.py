# Two Sum : Check if a pair with given sum exists in Array
'''
Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.
Examples:
Input: N = 5, arr[] = {2,6,5,8,11}, target = 14
Output : YES
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for first variant for second variant output will be : [1,3].
Input: N = 5, arr[] = {2,6,5,8,11}, target = 15
Output : NO.
Explanation: There exist no such two numbers whose sum is equal to the target.
'''
class Solution:
    # Brute force
    def two_sum1(self, array, size, target):
        for i in range(size):
            for j in range(i + 1, size):
                if(array[i] + array[j] == target):
                    return "YES"
        return "NO"
    
    # Better
    def two_sum2(self, array, size, target):
        hashMap = {}
        for i in range(size):
            element = array[i]
            moreRequired = target - element
            if moreRequired in hashMap:
                return "YES"
                # return [hashMap[moreRequired], i]
            hashMap[element] = i
        return "NO"
    
    # Optimal
    def two_sum3(self, array, size, target):
        left = 0
        right = size - 1
        array.sort()
        while(left < right):
            calculatedSum = array[left] + array[right]
            if calculatedSum == target:
                return "YES"
            elif calculatedSum < target:
                left = left + 1
            else:
                right = right - 1
        return "NO"
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
target = int(input("Enter the target: "))

object = Solution()
result = object.two_sum3(array, size, target)

print(result)