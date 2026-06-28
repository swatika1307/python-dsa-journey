# Find the highest/lowest frequency element
'''
Given an array of size N. Find the highest and lowest frequency element.
Examples:
Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.
Example 2:
Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.
'''

class Solution:
    def highest_and_lowest_frequency1(self, array):
        key_value = {}
        for i in array:
            if i in key_value:
                key_value[i] += 1
            else:
                key_value[i] = 1
        for key, value in key_value.items():
            print(f"Element {key} appears {value} times.")
        maxi_key, maxi_value = None, 0
        mini_key, mini_value = None, float('inf')
        for key, value in key_value.items(): 
            if value > maxi_value:
                maxi_value = value
                maxi_key = key
            if value < mini_value:
                mini_value = value
                mini_key = key
        print("Maximum frequency element:", maxi_key)
        print("Minimum frequency element:", mini_key)

        # More than one element being maximum
    def highest_and_lowest_frequency2(self, array):
        key_value = {}
        for i in array:
            if i in key_value:
                key_value[i] += 1
            else:
                key_value[i] = 1         
        for key, value in key_value.items():
            print(f"Element {key} appears {value} times.")    
        maxi_keys, maxi_value = [], 0
        mini_keys, mini_value = [], float('inf')
        for key, value in key_value.items():
            # Maximum
            if value > maxi_value:
                maxi_value = value
                maxi_keys = [key]  # Found a strictly higher frequency! Reset list
            elif value == maxi_value:
                maxi_keys.append(key)  # It's a tie! Append to existing list
            # Minimum
            if value < mini_value:
                mini_value = value
                mini_keys = [key]  # Found a strictly lower frequency! Reset list
            elif value == mini_value:
                mini_keys.append(key)  # It's a tie! Append to existing list
        print("Maximum frequency element:", maxi_keys)
        print("Minimum frequency element:", mini_keys)

array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
object.highest_and_lowest_frequency2(array)