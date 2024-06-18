from typing import Optional, Set
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        def in_order_traversal(node: Optional[TreeNode], elements: deque):
            if not node:
                return
            in_order_traversal(node.left, elements)
            elements.append(node.val)
            in_order_traversal(node.right, elements)
        
        elements = deque()
        in_order_traversal(root, elements)
        
        left, right = 0, len(elements) - 1
        
        while left < right:
            current_sum = elements[left] + elements[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return False