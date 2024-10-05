class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key: (day, ownStock) pair, value = max profit
        dp[-1, True] = float(-inf)
        dp[-1, False] = 0

        for day, price in enumerate(prices):
            dp[day, True] = max(dp[day - 1, True], dp[day - 1, False] - price)
            dp[day, False] = max(dp[day - 1, False], dp[day - 1, True] + price)
        
        return dp[len(prices) - 1, False]