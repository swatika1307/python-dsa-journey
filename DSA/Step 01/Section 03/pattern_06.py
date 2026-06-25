# Pattern 06 - 
'''
1 2 3 4
1 2 3
1 2 
1
for rows = 4
'''

class Solution:
    def pattern_06(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, rows + 2 - i):
                    print(j, end = ' ')
                print()

pattern = Solution()
pattern.pattern_06()