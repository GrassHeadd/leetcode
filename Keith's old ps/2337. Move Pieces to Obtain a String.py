class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sIndex, tIndex = 0, 0
        while sIndex < len(start) or tIndex < len(target):
            # Skip underscores in both strings
            while sIndex < len(start) and start[sIndex] == "_":
                sIndex += 1
            while tIndex < len(target) and target[tIndex] == "_":
                tIndex += 1

            # Check if both pointers are out of bounds (end of strings)
            if sIndex == len(start) and tIndex == len(target):
                return True
            if sIndex == len(start) or tIndex == len(target):
                return False

            # Check if characters mismatch
            if start[sIndex] != target[tIndex]:
                return False

            # Validate positions based on character
            if start[sIndex] == "L" and sIndex < tIndex:
                return False
            if start[sIndex] == "R" and sIndex > tIndex:
                return False

            sIndex += 1
            tIndex += 1

        return True
