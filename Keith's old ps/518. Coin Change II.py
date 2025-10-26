class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins: # change to loop coin outside to prevent permutation
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]