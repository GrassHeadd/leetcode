# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        ans = []
        while q:
            s = len(q)
            m = float('-inf')
            for _ in range(s):
                node = q.popleft()
                m = max(node.val, m)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(m)
        return ans
