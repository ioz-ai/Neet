#You are given the root of a binary tree root. Invert the binary tree and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        inv = None

        if root:
            inv = TreeNode()
            if root.right is not None:
                inv.left = self.invertTree(root.right)
            inv.val = root.val
            if root.left is not None:
                inv.right = self.invertTree(root.left)

            
        return inv