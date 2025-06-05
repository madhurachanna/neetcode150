"""
Stock Buy And Sell

You are given an array prices where prices[i] is the price of a given
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""
from typing import List

def bs_stocks(prices: List) -> int:
    buy_at = 1000000
    max_profits = 0


    for price in prices:
        if price < buy_at:
            buy_at = price
            continue
        max_profits = max(max_profits, price - buy_at)

    return max_profits


op = bs_stocks([7,6,4,3,1])
print(op)
