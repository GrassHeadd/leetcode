class Solution:
    def minSwaps(self, s: str) -> int:
        openCounter = 0
        mismatch = 0

        for c in s:
            if c == "[":
                openCounter += 1
            else:
                if openCounter > 0:
                    openCounter -= 1
                else:
                    mismatch += 1
        
        return math.floor((mismatch + 1) / 2)

                