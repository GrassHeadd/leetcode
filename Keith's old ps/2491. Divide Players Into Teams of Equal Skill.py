class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total = sum(skill)

        if total % (n // 2) != 0:
            return -1
        
        target = total // (n // 2)
        result = 0
        freq = {}

        for s in skill:
            if target - s in freq and freq[target - s] > 0:
                freq[target - s] -= 1
                result += s * (target - s)
            else:
                freq[s] = freq.get(s, 0) + 1
        
        for count in freq.values():
            if count > 0:
                return -1
        return result

        