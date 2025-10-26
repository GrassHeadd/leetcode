class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split(" ")
        for i, s in enumerate(arr):
            if s.startswith(searchWord):
                return i + 1
        return -1
