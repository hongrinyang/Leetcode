class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf_sequence(root, sequence):
            if not root:
                return
            if not root.left and not root.right:
                sequence.append(root.val)
            get_leaf_sequence(root.left, sequence)
            get_leaf_sequence(root.right, sequence)
        
        sequence1, sequence2 = [], []
        get_leaf_sequence(root1, sequence1)
        get_leaf_sequence(root2, sequence2)
        
        return sequence1 == sequence2