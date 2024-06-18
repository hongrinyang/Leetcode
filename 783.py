# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # List to store inorder traversal result
        inorder_values = []
        
        # Function to perform inorder traversal
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_values.append(node.val)
            inorder(node.right)
        
        # Perform inorder traversal to populate inorder_values
        inorder(root)
        
        # Calculate minimum difference
        min_diff = float('inf')
        for i in range(1, len(inorder_values)):
            min_diff = min(min_diff, inorder_values[i] - inorder_values[i - 1])
        
        return min_diff
