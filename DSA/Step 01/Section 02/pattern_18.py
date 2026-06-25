# Pattern 18 - 
'''
D
C D
B C D
A B C D
for rows = 4
'''

class Solution:
    def pattern_18(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                count = rows + 1 - i
                for j in range(1, i + 1):
                    print(chr(count + 64), end = ' ')
                    count += 1
                print()

pattern = Solution()
pattern.pattern_18()