# If array has positives and negatives
class Solution:
    # Brute force
    def longest_subarray_with_sum_k1(self, array, size, k):
        len = 0
        for i in range(size):
            required_sum = 0
            for j in range(i, size):
                required_sum = required_sum + array[j]
                if required_sum == k:
                    len = max(len, j - i + 1)
        return len
    
    # Optimal
    def longest_subarray_with_sum_k1(self, array, size, k):
        prefixSum = 0
        maxLength = 0
        hashMap = {}
        for i in range(size):
            prefixSum = prefixSum + array[i]
            if prefixSum == k:
                maxLength = max(maxLength, i + 1)
            rem = prefixSum - k
            if rem in hashMap:
                len = i - hashMap[rem]
                maxLength = max(maxLength, len)
            if prefixSum not in hashMap:
                hashMap[prefixSum] = i
        return maxLength
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
k = int(input("Enter the required sum: "))

object = Solution()
result = object.longest_subarray_with_sum_k3(array, size, k)

print(result)