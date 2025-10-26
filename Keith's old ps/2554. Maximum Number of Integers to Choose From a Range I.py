class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  # Convert list to set for faster lookup
        curr, count = 0, 0
        for i in range(1, n + 1):
            if i in banned_set:  # Faster lookup
                continue
            if curr + i <= maxSum:
                curr += i
                count += 1
            else:
                break  # Early exit if maxSum is exceeded
        return count
