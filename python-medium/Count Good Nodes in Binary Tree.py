
# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

# Given the root of a binary tree root, return the number of good nodes within the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def countg(self, root: TreeNode, goodval:float) -> int:
        if root is None:
            return 0
        if goodval <= root.val:
            return 1 + self.countg(root.left, max(root.val, goodval)) + self.countg(root.right, max(root.val, goodval))
        return self.countg(root.left, goodval) + self.countg(root.right, goodval)

    def goodNodes(self, root: TreeNode) -> int:
        return self.countg(root, float('-inf'))
