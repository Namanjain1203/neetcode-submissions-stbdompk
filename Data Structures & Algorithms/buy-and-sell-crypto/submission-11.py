class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_p = 0
        for p in prices:
            min_price = min(p,min_price)
            prof = p - min_price
            max_p = max(prof,max_p)
        return max_p        