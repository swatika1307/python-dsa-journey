# Leaders in an Array
'''
Examples:
Example 1:
Input: arr = [4, 7, 1, 0]  
Output: 7 1 0  
Explanation: The rightmost element (0) is always a leader. 7 and 1 are greater than the elements to their right, making them leaders as well.
Example 2:
Input: arr = [10, 22, 12, 3, 0, 6]  
Output: 22 12 6  
Explanation: 6 is a leader because there are no elements after it. 12 is greater than all the elements to its right (3, 0, 6), and 22 is greater than 12, 3, 0, 6, making them leaders as well.
'''

class Solution:
    # Brute force
    def leaders_in_an_array1(self, array, size):
        ans = []
        for i in range(size):
            leader = True
            for j in range(i + 1, size):
                if(array[j] > array[i]):
                    leader = False
                    break
            if(leader == True):
                ans.append(array[i])
            ans.sort()
        return ans
    
    # Optimal
    def leaders_in_an_array2(self, array, size):
        ans = []
        maxi = float('-inf')
        for i in range(size - 1, -1, -1):
            if(array[i] > maxi):
                ans.append(array[i])
            maxi = max(maxi, array[i])
        ans.sort()
        return ans

array = []
size = int(input("Enter the size: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.leaders_in_an_array2(array, size)

for i in range(len(result)):
    print(result[i], end = ' ')