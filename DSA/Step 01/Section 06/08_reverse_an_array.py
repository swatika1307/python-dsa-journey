# Reverse a given Array
'''
You are given an array. The task is to reverse the array and print it.
Examples:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.
'''

class Solution:
    # Approach 1 :
    def reverse_an_array1(self, array, left, right):
        if(left >= right):
            return
        array[left], array[right] = array[right], array[left]
        self.reverse_an_array1(array, left + 1, right - 1)

    # Approach 2 :
    def reverse_an_array2(self, array, i, size):
        if(i >= size // 2):
            return
        array[i], array[size - i - 1] = array[size - i - 1], array[i]
        self.reverse_an_array2(array, i + 1, size)


size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
obj = Solution()
obj.reverse_an_array2(array, 0, size)
for i in range(size):
    print(array[i], end = ' ')