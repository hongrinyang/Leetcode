class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev_val = float('-inf')
        self.min_diff = float('inf')
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            current_val = node.val
            self.min_diff = min(self.min_diff, current_val - self.prev_val)
            self.prev_val = current_val
            
            inorder(node.right)

        inorder(root)
        
        return self.min_diff
