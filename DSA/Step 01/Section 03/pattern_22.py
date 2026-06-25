class Solution:
    def pattern_22(self):
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            rows = int(input("Enter the number of rows: "))
            for i in range(1, (2 * rows)):
                for j in range(1, (2 * rows)):
                    top = i
                    left = (2 * rows) - i
                    bottom = j
                    right = (2 * rows) - j
                    value = min(top, left, bottom, right)
                    print(rows - value + 1, end = ' ')
                print()
    
pattern = Solution()
pattern.pattern_22()                