class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        # Initialize the dp array to a large number, dp[0] = 0 (no extra chars at the start)
        dp = [999999] * (n + 1)
        dp[0] = 0

        # Iterate over every position in the string
        for i in range(1, n + 1):
            # Assume the current character s[i-1] is extra
            dp[i] = dp[i - 1] + 1

            # Check if any word in the dictionary matches the substring ending at i
            for w in dictionary:
                # Only proceed if there's space for the word before i
                if i >= len(w) and s[i - len(w):i] == w:
                    dp[i] = min(dp[i], dp[i - len(w)])

        return dp[n]