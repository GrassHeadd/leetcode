class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(w1, w2):
            n1, n2 = len(w1), len(w2)
            if n1 > n2:
                return False
            # Check if w1 is a prefix and a suffix of w2
            return w2.startswith(w1) and w2.endswith(w1)
        
        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count
