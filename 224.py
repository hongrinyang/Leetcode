class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # Stack to store previous results and signs
        result = 0  # Current result
        sign = 1  # 1 for positive, -1 for negative
        num = 0  # Current number being formed

        for char in s:
            if char.isdigit():  # Build the current number
                num = num * 10 + int(char)
            elif char == '+':  # If +, we add the number to result
                result += sign * num
                sign = 1  # Reset sign to positive for next number
                num = 0  # Reset num to 0 for the next number
            elif char == '-':  # If -, we subtract the number from result
                result += sign * num
                sign = -1  # Set sign to negative for next number
                num = 0  # Reset num to 0 for the next number
            elif char == '(':  # Push the current result and sign to the stack
                stack.append(result)
                stack.append(sign)
                result = 0  # Reset result for the new sub-expression
                sign = 1  # Reset sign for the sub-expression
            elif char == ')':  # Pop the result and sign from the stack
                result += sign * num
                num = 0  # Reset num
                result *= stack.pop()  # Apply the sign before the parenthesis
                result += stack.pop()  # Apply the result before the parenthesis

        result += sign * num  # Add the last number
        return result
