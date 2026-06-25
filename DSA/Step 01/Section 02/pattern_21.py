# Problem 21 -
'''
* * * *
* _ _ *
* _ _ *
* * * *
for rows = 4
'''

class Solution:
    def pattern_21(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, rows + 1):
                    if((i == 1) or (j == 1) or (j == rows) or (i == rows)):
                        print("* ", end = '')
                    else:
                        print("_ ", end = '')
                print()

pattern = Solution()
pattern.pattern_21()