# Pattern 05 - 
'''
* * * *
* * *
* * 
*
for rows = 4
'''

class Solution:
    def pattern_05(self):
        test_cases = int(input("Enter thenumber of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(rows + 1, i, -1):
                    print("*", end = ' ')
                print()

pattern = Solution()
pattern.pattern_05()