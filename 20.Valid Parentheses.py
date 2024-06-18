class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold matching pairs
        bracket_pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_pairs.values():
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
            elif char in bracket_pairs.keys():
                # If it's a closing bracket, check if it matches the top of the stack
                if stack and stack[-1] == bracket_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Invalid character
                return False
        
        # If the stack is empty, all brackets were matched correctly
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))        # Output: true
print(solution.isValid("()[]{}"))    # Output: true
print(solution.isValid("(]"))        # Output: false
print(solution.isValid("([)]"))      # Output: false
print(solution.isValid("{[]}"))      # Output: true
