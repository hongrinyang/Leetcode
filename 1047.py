class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            if stack and stack[-1] == char:
                # If the top of the stack matches the current character, pop the stack
                stack.pop()
            else:
                # Otherwise, push the current character onto the stack
                stack.append(char)
        
        # Join the stack to form the final string
        return ''.join(stack)
