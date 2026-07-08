# Rearrange Array Elements by Sign
'''
There's an array A of size N with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
Examples:
Example 1:
Input: arr[] = {1,2,-4,-5}, N = 4
Output: 1 -4 2 -5
Explanation: 
Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.
'''

class Solution:
    # Brute force
    def rearrange_elements_same_size1(self, array, size):
        pos = []
        neg = []
        for i in range(size):
            if(array[i] > 0):
                pos.append(array[i])
            else:
                neg.append(array[i])
        for i in range(size // 2):
            array[2 * i] = pos[i]
            array[(2 * i) + 1] = neg[i]
        return array
    
    # Optimal
    def rearrange_elements_same_size2(self, array, size):
        ans = [0] * size
        pos = 0
        neg = 1
        for i in range(size):
            if(array[i] > 0):
                ans[pos] = array[i]
                pos = pos + 2
            else:
                ans[neg] = array[i]
                neg = neg + 2
        return ans
    
array = []
size = int(input("Enter the size: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.rearrange_elements_same_size2(array, size)

for i in range(len(result)):
    print(result[i], end = ' ')