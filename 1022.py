class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, current_value):
            # If the node is None, return 0 (base case for null nodes)
            if not node:
                return 0
            
            # Update the current value by shifting left (equivalent to multiplying by 2)
            # and adding the current node's value (either 0 or 1)
            current_value = (current_value << 1) | node.val
            
            # If it's a leaf node, return the current value
            if not node.left and not node.right:
                return current_value
            
            # Otherwise, continue DFS on both left and right subtrees
            return dfs(node.left, current_value) + dfs(node.right, current_value)
        
        # Call DFS starting from the root with initial value 0
        return dfs(root, 0)
