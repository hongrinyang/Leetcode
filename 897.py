# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal and collect nodes.
        def in_order(node):
            if not node:
                return []
            return in_order(node.left) + [node] + in_order(node.right)
        
        # Collect nodes in in-order (sorted order)
        nodes = in_order(root)
        
        # Create a new tree where each node has only right child
        dummy = TreeNode(0)
        current = dummy
        
        for node in nodes:
            node.left = None  # Ensure no left child
            current.right = node  # Link current node's right child to the next node
            current = node  # Move to the next node
        
        # Return the new root, which is the right child of the dummy node
        return dummy.right
