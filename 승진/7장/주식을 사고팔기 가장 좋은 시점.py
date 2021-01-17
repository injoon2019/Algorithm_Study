from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for price in prices[1:]:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
