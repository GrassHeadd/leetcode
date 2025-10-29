from common_imports import *

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        print(c)
        res = 0

        for i in c:
            if k == 2 * i:
                n = c[i] // 2
                res += n
            elif k - i in c:
                n = max(c[k - i], c[i])
                res += n
                c[k - i] -= n
                c[i] -= n

        return res