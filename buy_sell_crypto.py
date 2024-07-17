"""
Buy and Sell Crypto

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions,
in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
"""

# O(n^2) || O(nlogn)
def get_max_profit_after_trading_2(prices):
    max_profits = 0

    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_profits = max(max_profits, prices[j] - prices[i])

    return max_profits


# O(n)
def get_max_profit_after_trading(prices):
    max_profits = 0
    i = 0
    j = i + 1

    # Start calculating profits
    # If we find a better buying situvation (prices[j] < prices[i])
    # Start finding max profits from that position
    while j < len(prices):
        max_profits = max(max_profits, prices[j] - prices[i])
        if (prices[j] < prices[i]):
            i = j
            j += 1
        else:
            j += 1

    return max_profits



# prices = [10,1,5,6,7,1]
# prices = [10,8,7,5,2]
# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [2,1,4]
# prices = [2,3,1,4]
# op = get_max_profit_after_trading(prices)
# print(op)
