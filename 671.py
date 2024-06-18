class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root):
        def dfs(node):
            if node:
                values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        values = set()
        dfs(root)

        # If there are fewer than 2 unique values, return -1
        if len(values) < 2:
            return -1

        # Find the second minimum value
        min_val = root.val
        second_min = float('inf')
        for val in values:
            if val > min_val and val < second_min:
                second_min = val

        return second_min if second_min != float('inf') else -1
