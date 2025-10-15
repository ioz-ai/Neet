# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if n == 0:
            return head
        
        ptrs = []
        p = head
        while p is not None:
            ptrs.append(p)
            p = p.next

        N = len(ptrs)

        if N-n  == 0:
            # remove the head (ptrs[0])
            return head.next

        ptrs[N-n-1].next = ptrs[N-n].next

        return head