# Move all Zeros to the end of the array
'''
You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.
Examples:
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Input : 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
'''

class Solution:
    # Brute force
    def move_all_zeros_to_the_end1(self, array, size):
        temp = []
        for i in range(size):
            if(array[i] != 0):
                temp.append(array[i])
        for i in range(len(temp)):
            array[i] = temp[i]
        for i in range(len(temp), size):
            array[i] = 0
    
    # Optimal
    def move_all_zeros_to_the_end2(self, array, size):
        j = -1
        for i in range(size):
            if(array[i] == 0):
                j = i
                break
        for i in range(j + 1, size):
            if(array[i] != 0):
                array[i], array[j] = array[j], array[i]
                j = j + 1
        
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.move_all_zeros_to_the_end2(array, size)

for i in range(size):
    print(array[i], end = ' ')