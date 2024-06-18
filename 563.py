class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0
        
        def calculateTilt(node):
            if not node:
                return 0
            
            left_sum = calculateTilt(node.left)
            right_sum = calculateTilt(node.right)
            
            tilt = abs(left_sum - right_sum)
            self.total_tilt += tilt
            
            return node.val + left_sum + right_sum
        
        calculateTilt(root)
        
        return self.total_tilt
