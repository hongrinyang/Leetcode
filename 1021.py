class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        
        for char in s:
            if char == '(':
                # Before increasing depth, check if it's an outer parenthesis
                if depth > 0:
                    result.append(char)
                depth += 1
            elif char == ')':
                # Before decreasing depth, check if it's an outer parenthesis
                depth -= 1
                if depth > 0:
                    result.append(char)
        
        return ''.join(result)

# Example usage:
solution = Solution()

# Test case 1
s1 = "(()())(())"
print(solution.removeOuterParentheses(s1))  # Output: "()()()"

# Test case 2
s2 = "(()())(())(()(()))"
print(solution.removeOuterParentheses(s2))  # Output: "()()()()(())"

# Test case 3
s3 = "()()"
print(solution.removeOuterParentheses(s3))  # Output: ""
