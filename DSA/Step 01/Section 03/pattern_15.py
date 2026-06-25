# Pattern 15 - 
'''
A B C D
A B C
A B 
A
for rows = 4
'''

class Solution:
    def pattern_15(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(rows, 0, -1):
                for j in range(1, i + 1):
                    print(chr(64 + j), end = ' ')
                print()

pattern = Solution()
pattern.pattern_15()