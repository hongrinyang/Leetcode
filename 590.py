class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.insert(0, node.val)  # Insert at the beginning for postorder
            # Push children in regular order to process leftmost first
            for child in node.children:
                stack.append(child)
        
        return result