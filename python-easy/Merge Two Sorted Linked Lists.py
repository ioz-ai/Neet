
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        m = None
        m1 = m
        while list1 or list2:
            
            h3 = None
            if list1 is None:
                h3 = list2
                list2 = list2.next
            elif list2 is None:
                h3 = list1
                list1 = list1.next
            elif list1.val >= list2.val:
                h3 = list2
                list2=list2.next
            else:
                h3 = list1
                list1 = list1.next
           

            if m is None:
                m = ListNode(h3.val)
                m1 = m
            else:
                m1.next = ListNode(h3.val)
                m1 = m1.next

        return m
