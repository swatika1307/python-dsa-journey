# Pattern 13 - 
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
for rows = 5
'''

class Solution:
    def pattern_13(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            count = 1
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print(count, end = ' ')
                    count += 1
                print()

pattern = Solution()
pattern.pattern_13()