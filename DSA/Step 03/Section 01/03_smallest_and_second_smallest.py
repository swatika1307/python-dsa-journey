class Solution:
    def smallest_and_second_smallest(self, array, size):
        smallest = array[0]
        secondSmallest = float('inf')
        for i in range(1, size):
            if(array[i] < smallest):
                secondSmallest = smallest
                smallest = array[i]
            elif(array[i] > smallest and array[i] < secondSmallest):
                secondSmallest = array[i]
        return [smallest, secondSmallest]

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.smallest_and_second_smallest(array, size)

print("Smallest element is:", result[0])
print("Second smallest element is:", result[1])