class Solution:
    def binaryTreePaths(self, root):
        def dfs(node, path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                paths.append("->".join(path))
            else:
                dfs(node.left, path[:])
                dfs(node.right, path[:])

        paths = []
        dfs(root, [])
        return paths