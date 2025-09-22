# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

# The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

# Given the root of a binary tree root, return the diameter of the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # Update the max_diameter with the path that goes through the current node
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return the height of the current subtree
            return 1 + max(left_height, right_height)

        height(root)
        return self.max_diameter