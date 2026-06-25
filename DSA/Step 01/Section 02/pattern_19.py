# Pattern 19 -
'''
* * * * * * * * * *
* * * * _ _ * * * *
* * * _ _ _ _ * * *
* * _ _ _ _ _ _ * *
* _ _ _ _ _ _ _ _ *
* _ _ _ _ _ _ _ _ *
* * _ _ _ _ _ _ * *
* * * _ _ _ _ * * *
* * * * _ _ * * * *
* * * * * * * * * * 
for rows = 5
'''

class Solution:
    def pattern_19(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(rows, i - 1, -1):
                    print("* ", end = '')
                for spaces in range((2 * i) - 2):
                    print("_ ", end = '')
                for j in range(rows, i - 1, -1):
                    print("* ", end = '')
                print()
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print("* ", end = '')
                for spaces in range(1, (2 * (rows - i) + 1)) :
                    print("_ ", end = '')
                for j in range(1, i + 1):
                    print("* ", end = '')
                print()

pattern = Solution()
pattern.pattern_19()