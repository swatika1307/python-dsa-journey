class Solution:
    # only if the string has lower case characters
    def character_hashing1(self, string):
        hashArray = [0] * 26
        for i in range(len(string)):
            val = ord(string[i]) - ord('a')
            hashArray[val] = hashArray[val] + 1
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            ch = input("Enter the character: ")
            print(hashArray[ord(ch) - ord('a')])

    # if the string has upper case and lower case characters
    def character_hashing2(self, string):
        hashArray = [0] * 256
        for i in range(len(string)):
            val = ord(string[i])
            hashArray[val] = hashArray[val] + 1
        test_cases = int(input("Enter the number of test cases: "))
        for _ in range(test_cases):
            ch = input("Enter the character: ")
            print(hashArray[ord(ch)])
            
object = Solution()
string = input("Enter the string: ")
object.character_hashing1(string)