# Pattern 09 - 
'''
_ _ _ * _ _ _
_ _ * * * _ _
_ * * * * * _
* * * * * * *
* * * * * * *
_ * * * * * _
_ _ * * * _ _
_ _ _ * _ _ _
for rows = 4
_ = space
'''

class Solution:
    def pattern_09(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for spaces in range(1, rows + 1 - i):
                    print("_", end = '')
                for j in range(2 * i - 1):
                    print("*", end = '')
                for spaces in range(1, rows + 1 - i):
                    print("_", end = '')
                print()
            for i in range(1, rows + 1):
                for spaces in range(1, i):
                    print("_", end = '')
                for j in range((2 *(rows - i)) + 1):
                    print("*", end = '')
                for spaces in range(1, i):
                    print("_", end = '')
                print()

pattern = Solution()
pattern.pattern_09()