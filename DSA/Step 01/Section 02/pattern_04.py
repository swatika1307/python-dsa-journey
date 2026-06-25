# Pattern 04 - 
'''
1 
2 2 
3 3 3
4 4 4 4
for rows = 4
'''

class Solution:
    def pattern_04(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print(i, end = ' ')
                print()

pattern = Solution()
pattern.pattern_04()