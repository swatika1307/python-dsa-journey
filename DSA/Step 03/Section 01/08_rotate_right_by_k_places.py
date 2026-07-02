class Solution:
    def reverse(self, array, start, end):
        while(start < end):
            array[start], array[end] = array[end], array[start]
            start = start + 1
            end = end - 1

    def rotate_right_by_k_places(self, array, size, k):
        k = k % size
        self.reverse(array, 0, size - 1)
        self.reverse(array, 0, k - 1)
        self.reverse(array, k, size - 1)

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)
k = int(input("Enter the number of places by which you want to left rotate the array: "))

object = Solution()
result = object.rotate_right_by_k_places(array, size, k)

for i in range(size):
    print(array[i], end = ' ')