class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float('inf')
        max_profit = 0
        for price in prices:
            min_prices = min(min_prices,price)
            profit = price - min_prices
            max_profit = max(max_profit,profit)
        return max_profit