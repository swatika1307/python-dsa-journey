# Check if the given String is Palindrome or not
'''
Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.
Examples:
Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.
Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.
'''
class Solution:
    def check_string_palindrome(self, i, string):
        if(i >= len(string) // 2):
            return True
        if(string[i] != string[len(string) - i - 1]):
            return False
        return self.check_string_palindrome(i + 1, string)

string = input("Enter the string: ")
object = Solution()
result = object.check_string_palindrome(0, string)
print(result)