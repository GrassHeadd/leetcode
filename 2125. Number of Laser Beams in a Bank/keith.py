from common_imports import *

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, cur, res = 0, 0, 0
        for row in bank:
            cur = row.count('1')
            if cur == 0:
                continue
            print(cur, prev)
            res += cur * prev
            prev, cur = cur, 0
        return res
        