class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, a):
        cur = self.root
        tmp = str(a)
        for ch in tmp:
            num = int(ch)
            if num not in cur.child:
                cur.child[num] = TrieNode()
            cur = cur.child[num]
        cur.is_end = True

    def prefix_match(self, b):
        cur = self.root
        tmp = str(b)
        length = 0
        for ch in tmp:
            num = int(ch)
            if num not in cur.child:
                break
            cur = cur.child[num]
            length += 1
        return length
    

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = Trie()
        for val in arr1:
            t.insert(val)
        
        mx = 0
        for val in arr2:
            mx = max(mx, t.prefix_match(val))

        return mx
        