class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Greedy algo, recursively add?
        total = target[0]
        for i in range(len(target) - 1):
            diff = target[i + 1] - target[i]
            if (diff) > 0:
                total += diff

        return total
