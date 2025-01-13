class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        res = 0

        for letter in freq:
            if freq[letter] % 2 == 0:
                res += 2
            else:
                res += 1

        return res
        