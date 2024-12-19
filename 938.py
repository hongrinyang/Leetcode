class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Base case: if the root is None, return 0
        if not root:
            return 0
        
        total_sum = 0
        
        # If the node's value is within the range, add it to the total sum
        if low <= root.val <= high:
            total_sum += root.val
        
        # If the node's value is greater than low, check the left subtree
        if root.val > low:
            total_sum += self.rangeSumBST(root.left, low, high)
        
        # If the node's value is less than high, check the right subtree
        if root.val < high:
            total_sum += self.rangeSumBST(root.right, low, high)
        
        return total_sum
