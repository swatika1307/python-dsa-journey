class Solution:
    def hashing(self, array):
        # Pre-compute
        hashArray = [0] * 13
        for i in range(len(array)):
            hashArray[array[i]] = hashArray[array[i]] + 1
            
        test_cases = int(input("Enter the number of test cases: "))
        for i in range(test_cases):
            number = int(input("Enter the number: "))
            # Fetching
            print(hashArray[number])

size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

obj = Solution()
obj.hashing(array)