# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        # Base Case 2: If one node is None, or their values are different,
        # they are not identical.
        if not p or not q or p.val != q.val:
            return False
            
        # Recursive Step: The trees are the same only if BOTH their left
        # and right subtrees are also the same.
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))