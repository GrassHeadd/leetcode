class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = str(bin(n)).lstrip('0b')
        binary = binary.replace('0', '1')
        return int(binary, 2)