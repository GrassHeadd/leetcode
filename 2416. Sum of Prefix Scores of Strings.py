class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
            cur.count += 1            
    
    def find(self, word):
        cur = self.root
        total_count = 0
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
            total_count += cur.count
        return total_count   

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        for val in words:
            t.insert(val)
        
        n = len(words)
        result = [0] * n
        for i in range(0, n):
            result[i] = t.find(words[i])

        return result
        