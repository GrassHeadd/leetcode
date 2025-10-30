from common_imports import *

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev, res = 0, 0
        for i in target:
            if i > prev:
                res += i - prev
            prev = i
        return res

        # Approach 1
        # def solve(arr):
        #     if not arr:
        #         return 0
        #     m = min(arr)
        #     arr = [x - m for x in arr]
        #     total = m

        #     # split
        #     i, n = 0, len(arr)
        #     while i < n:
        #         while i < n and arr[i] == 0:
        #             i += 1
        #         if i >= n:
        #             break

        #         j = i
        #         while j < n and arr[j] > 0:
        #             j += 1
        #         total += solve(arr[i:j])
        #         i = j
        #     return total
        # return solve(target)