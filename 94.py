class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        stack = []
        current = root
        result = []
        
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Current must be None at this point
            current = stack.pop()
            result.append(current.val)
            
            # Visit the right subtree
            current = current.right
        
        return result