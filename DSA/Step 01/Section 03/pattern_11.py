# Pattern 11 - 
'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
for rows = 5
'''

class Solution:
    def pattern_11(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    if(((i % 2 != 0) and (j % 2 != 0)) or ((i % 2 == 0) and (j % 2 == 0))):
                        print("1 ", end ='')
                    else:
                        print("0 ", end = '')
                print()

pattern = Solution()
pattern.pattern_11()