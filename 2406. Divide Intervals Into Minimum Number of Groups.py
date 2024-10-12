class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append([start, 1])
            time.append([end + 1, -1])
        res = cur = 0
        for i, diff in sorted(time):
            cur += diff
            res = max(res, cur)
        return res