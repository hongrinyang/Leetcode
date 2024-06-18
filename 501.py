class Solution:
    def findMode(self, root):
        if not root:
            return []
        
        self.modes = []
        self.max_count = 0
        self.cur_val = None
        self.cur_count = 0
        self.inorder(root)

        if self.cur_count > self.max_count:
            self.modes = [self.cur_val]
        elif self.cur_count == self.max_count:
            self.modes.append(self.cur_val)
        
        return self.modes
    
    def inorder(self, node):
        if not node:
            return
        
        self.inorder(node.left)

        if node.val == self.cur_val:
            self.cur_count += 1
        else:
            if self.cur_count > self.max_count:
                self.max_count = self.cur_count
                self.modes = [self.cur_val]
            elif self.cur_count == self.max_count:
                self.modes.append(self.cur_val)
            
            self.cur_val = node.val
            self.cur_count = 1
        
        self.inorder(node.right)
