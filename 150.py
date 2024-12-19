class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Integer division truncates towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]

# Example usage
solution = Solution()
tokens = ["2", "1", "+", "3", "*"]
result = solution.evalRPN(tokens)
print(result)
