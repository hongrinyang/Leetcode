class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node):
        # Push all left children of the node to the stack
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self):
        # Get the next node in the in-order traversal
        node = self.stack.pop()
        value = node.val
        # After visiting the node, push its right child and all its left descendants
        if node.right:
            self._push_left(node.right)
        return value
    
    def hasNext(self):
        # Check if there are more nodes to visit in the in-order traversal
        return len(self.stack) > 0
