class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        l = len(cuts)
        
        dp = [[0] * l for _ in range(l)]  # dp[i][j] will store the cost to cut between cuts[i] and cuts[j]

        def helper(i, j):
            if i + 1 >= j:
                return 0
            if dp[i][j]:
                return dp[i][j]
            
            min_cost = float('inf')
            for k in range(i + 1, j):
                # Compute the cost of making the cut at cuts[k] and recursively solve the subproblems
                cost = cuts[j] - cuts[i] + helper(i, k) + helper(k, j)
                min_cost = min(min_cost, cost)
            
            dp[i][j] = min_cost
            return dp[i][j]

        return helper(0, l - 1)
