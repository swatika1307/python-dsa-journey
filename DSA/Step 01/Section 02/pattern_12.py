# Pattern 12 - 
'''
1 _ _ _ _ _ _ 1
1 2 _ _ _ _ 2 1
1 2 3 _ _ 3 2 1
1 2 3 4 4 3 2 1
for rows = 4
_ = space
'''

class Solution:
    def pattern_12(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print(j, end = '')
                for spaces in range(1, rows - i + 1):
                    print("_", end = '')
                for spaces in range(1, rows - i + 1):
                    print("_", end = '')
                for j in range(i, 0, -1):
                    print(j, end = '')
                print()
        
pattern = Solution()
pattern.pattern_12()