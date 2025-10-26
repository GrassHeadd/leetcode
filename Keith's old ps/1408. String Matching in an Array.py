class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        merge = " ".join(words)
        ans = []
        for w in words:
            if merge.count(w) > 1:
                ans.append(w)

        return ans