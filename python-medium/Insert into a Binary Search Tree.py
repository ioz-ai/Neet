# You are given the root node of a binary search tree (BST) and a value val to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Note: There may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root

        p = root
        while p is not None:
            if val < p.val:
                if p.left == None:
                    # insert
                    p.left = TreeNode(val)
                    break
                else:
                    p = p.left
            elif val > p.val:
                if p.right == None:
                    #insert
                    p.right = TreeNode(val)
                    break
                else:
                    p = p.right

        return root
            