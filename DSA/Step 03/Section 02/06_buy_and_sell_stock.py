# Stock Buy And Sell
'''
You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note: That buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

class Solution:
    def buy_and_sell_stock(self, array, size):
        mini = array[0]
        profit = 0
        for i in range(1, size):
            cost = array[i] - mini
            profit = max(cost, profit)
            mini = min(mini, array[i])
        return profit
    
array = []
size = int(input("Enter the number of days: "))
for i in range(size):
    val = int(input("Enter the stock value: "))
    array.append(val)

object = Solution()
result = object.buy_and_sell_stock(array, size)

print("Profit:", result)