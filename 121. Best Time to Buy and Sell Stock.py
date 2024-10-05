class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ans = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                ans = max(ans, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return ans