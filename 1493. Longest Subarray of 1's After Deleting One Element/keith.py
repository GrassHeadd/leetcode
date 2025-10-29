from common_imports import *

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        i = 0
        hasZero = False
        for j in range(len(nums)):
            if nums[j] == 0:
                if hasZero:
                    while nums[i] != 0:
                        i += 1
                    i += 1         # Just after zero
                else:
                    hasZero = True
            res = max(res, j - i)
        return res
            