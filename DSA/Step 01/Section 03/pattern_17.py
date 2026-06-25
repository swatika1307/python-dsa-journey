# Pattern 17 - 
'''
_ _ _ A _ _ _
_ _ A B A _ _
_ A B C B A _
A B C D C B A
for rows = 4
_ = space
'''

class Solution:
    def pattern_17(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for spaces in range(rows - i, 0, -1):
                    print("_", end ='')
                for j in range(1, i + 1):
                    print(chr(64 + j), end = '')
                for j in range(1, i):
                    print(chr(64 + j), end = '')
                for spaces in range(rows - i, 0, -1):
                    print("_", end ='')    
                print()

pattern = Solution()
pattern.pattern_17()