# Pattern 14 - 
'''
A
A B
A B C
A B C D
for rows = 4
'''

class Solution:
    def pattern_14(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print(chr(64 + j), end = ' ')
                print()

pattern = Solution()
pattern.pattern_14()