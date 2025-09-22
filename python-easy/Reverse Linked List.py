#Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 'prev' starts as None because the new tail's next will be None.
        # 'current' starts at the beginning of the list.
        prev, current = None, head

        # Loop until we've processed every node.
        while current:
            # 1. Store the next node before we change any pointers.
            next_temp = current.next
            
            # 2. Reverse the pointer of the current node.
            current.next = prev
            
            # 3. Move the 'prev' and 'current' pointers one step forward.
            prev = current
            current = next_temp
        
        # When the loop ends, 'prev' is the new head of the reversed list.
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h2 = None
        head2 = h2
        h1 = head

        while h1:
            n = None
            if h1 != head:
                n = h2
            h2 = ListNode(h1.val, n)
            h1 = h1.next

        return h2



def print_linked_list(head):
    """Prints the values of a linked list."""
    items = []
    current = head
    while current:
        items.append(str(current.val))
        current = current.next
    print(" -> ".join(items))

def create_linked_list(items):
    """Creates a linked list from a Python list."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

   