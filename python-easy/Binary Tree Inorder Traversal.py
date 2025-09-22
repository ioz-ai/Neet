
# You are given the root of a binary tree, return the inorder traversal of its nodes' values.
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # Base case: If the node is None, stop and return.
        if root is None:
            return result
        
        # 1. Traverse the left subtree recursively.
        result.extend(self.inorderTraversal(root.left))
        
        # 2. Visit the root node.
        result.append(root.val)
        
        # 3. Traverse the right subtree recursively.
        result.extend(self.inorderTraversal(root.right))
        
        return result


    