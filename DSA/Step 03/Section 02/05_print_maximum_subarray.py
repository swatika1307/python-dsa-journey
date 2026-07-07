class Solution:
    def print_maximum_subarray_sum(self, array, size):
        sum = 0
        maxi = float('-inf')
        ansStart = -1
        ansEnd = -1
        for i in range(size):
            if sum == 0:
                start = i
            sum = sum + array[i]
            if(sum > maxi):
                maxi = sum
                ansStart = start
                ansEnd = i
            if(sum < 0):
                sum = 0
        return [ansStart, ansEnd]
    
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.print_maximum_subarray_sum(array, size)

print("Start index:", result[0])
print("End index:", result[1])