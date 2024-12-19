class NestedIterator:
    def __init__(self, nestedList):
        # The stack will store elements to be processed. Initialize with nestedList.
        self.stack = []
        self.flatten(nestedList)
    
    def flatten(self, nestedList):
        # Flatten the nested list into a stack (with the elements in reverse order for easy pop).
        for item in reversed(nestedList):
            self.stack.append(item)
    
    def next(self):
        # Get the next integer (pop the stack until an integer is found).
        return self.stack.pop().getInteger()
    
    def hasNext(self):
        # Keep popping from the stack until we find an integer or the stack is empty.
        while self.stack and not self.stack[-1].isInteger():
            # If the top element is a list, flatten it and pop its elements onto the stack.
            nested = self.stack.pop()
            self.flatten(nested.getList())
        # If the stack is empty, there's no next element; otherwise, it's an integer.
        return bool(self.stack and self.stack[-1].isInteger())
