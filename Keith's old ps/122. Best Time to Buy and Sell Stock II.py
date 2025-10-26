from common_imports import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key: (day, ownStock) pair, value = max profit
        dp[-1, True] = float(-inf)
        dp[-1, False] = 0

        for day, price in enumerate(prices):
            dp[day, True] = max(dp[day - 1, True], dp[day - 1, False] - price)
            dp[day, False] = max(dp[day - 1, False], dp[day - 1, True] + price)
        
        return dp[len(prices) - 1, False]
    
# Even faster solution through greedy approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # Traverse through prices list
        for i in range(1, len(prices)):
            # If the price on day i is higher than day i-1, we take the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit
