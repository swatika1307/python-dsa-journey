# Pattern 16 - 
'''
A
B B
C C C
D D D D
for rows = 4
'''

class Solution:
    def pattern_16(self):
        test_cases = int(input("Enter thenumber of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print(chr(64 + i), end = ' ')
                print()
    
pattern = Solution()
pattern.pattern_16()