from common_imports import *

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        zeroes = []
        prefix, suffix = 0, sum(nums)
        res = 0
        for idx, value in enumerate(nums):
            suffix -= value
            if value == 0:
                zeroes.append([prefix, suffix, idx])
            prefix += value
        
        for idx in zeroes:
            diff = abs(idx[0] - idx[1])
            if diff == 0:
                res += 2
            elif diff == 1:
                res += 1

        print(zeroes)
        return res