class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Base case: If root is None or root's value equals val, return root
        if not root or root.val == val:
            return root
        
        # If val is less than root's value, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If val is greater than root's value, search in the right subtree
        return self.searchBST(root.right, val)