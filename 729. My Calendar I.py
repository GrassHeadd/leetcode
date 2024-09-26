class TreeNode():
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        else:
            return self.insert(start, end, self.root)

    def insert(self, s, e, node):
        if s >= node.e:
            if node.right:
                return self.insert(s, e, node.right)
            else:
                node.right = TreeNode(s, e)
                return True
        elif e <= node.s:
            if node.left:
                return self.insert(s, e, node.left)
            else:
                node.left = TreeNode(s, e)
                return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)