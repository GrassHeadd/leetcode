from common_imports import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Get middle
        slow, fast = head, head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second part
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        # Compute twins
        res = 0
        while second.next:
            res = max(res, head.val + second.val)
            head = head.next
            second = second.next
        return res