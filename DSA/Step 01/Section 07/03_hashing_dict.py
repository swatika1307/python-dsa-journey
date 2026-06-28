class Solution:
    def hashing_dict(self, array):
        key_value = {}
        for i in array:
            if i in key_value:
                key_value[i] += 1
            else:
                key_value[i] = 1
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            number = int(input("Enter the number: "))
            print(key_value.get(number, 0))

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
object.hashing_dict(array)