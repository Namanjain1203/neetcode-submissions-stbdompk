class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      n = len(prices)
      i = 0
      max_profit = 0
      for j in range(1,n):
        if prices[i]<prices[j]:
            profit = prices[j]-prices[i]
            max_profit = max(max_profit,profit)
        else:
            i = j
      return max_profit