class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth, target, info):
            if not node:
                return
            if node.val == target:
                info.extend([parent, depth])
                return
            dfs(node.left, node, depth + 1, target, info)
            dfs(node.right, node, depth + 1, target, info)
        
        # Store parent and depth info for x and y
        x_info, y_info = [], []
        
        dfs(root, None, 0, x, x_info)
        dfs(root, None, 0, y, y_info)
        
        # Check if they are cousins
        return x_info[1] == y_info[1] and x_info[0] != y_info[0]
