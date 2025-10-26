class Solution:
    def minimumSteps(self, s: str) -> int:
        swap, black = 0, 0
        for b in s:
            if b == "0":
                swap += black
            else:
                black += 1

        return swap