# Pattern 20 -
'''
* _ _ _ _ _ _ _ _ *
* * _ _ _ _ _ _ * *
* * * _ _ _ _ * * *
* * * * _ _ * * * *
* * * * * * * * * *
* * * * _ _ * * * *
* * * _ _ _ _ * * *
* * _ _ _ _ _ _ * *
* _ _ _ _ _ _ _ _ *
'''

class Solution:
    def pattern_20(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print("* ", end = '')
                for spaces in range(2 * (rows - i)):
                    print("_ ", end = '')
                for j in range(1, i + 1):
                    print("* ", end = '')
                print()
            for i in range(rows - 1, 0, -1):
                for j in range(i, 0, -1):
                    print("* ", end = '')
                for spaces in range((2 * rows) - (2 * i)):
                    print("_ ", end = '')
                for j in range(i, 0, -1):
                    print("* ", end = '')
                print()


pattern = Solution()
pattern.pattern_20()