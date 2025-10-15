# Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

# A valid binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isValid(self, root: Optional[TreeNode], minv: float, maxv: float) -> bool:
        if root is None:
            return True
        if not (minv < root.val and root.val < maxv):
            return False
        return self.isValid(root.left, minv, root.val) and self.isValid(root.right, root.val, maxv)
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('+inf'))
           

