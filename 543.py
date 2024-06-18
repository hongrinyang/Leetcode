class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def findDiameter(node):
            if not node:
                return 0

            left_height = findDiameter(node.left)
            right_height = findDiameter(node.right)
            
            self.diameter = max(self.diameter, left_height + right_height)

            return max(left_height, right_height) + 1
        
        findDiameter(root)
        return self.diameter
