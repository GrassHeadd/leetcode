class Solution:
    def reverseWords(self, s: str) -> str:
        r = s[::-1]
        words = r.split()
        r_words = [w[::-1] for w in words]
        return " ".join(r_words)