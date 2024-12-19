class Solution:
    def diffWaysToCompute(self, expression: str):
        # Memoization dictionary
        memo = {}
        
        def compute(expression):
            # If the result for this expression is already computed, return it from the memo
            if expression in memo:
                return memo[expression]
            
            # If the expression is a number, return it as a list of one element
            if expression.isdigit():
                return [int(expression)]
            
            result = []
            # Iterate through the expression and split at each operator
            for i in range(len(expression)):
                if expression[i] in '+-*':
                    # Split the expression into two parts at the operator
                    left = expression[:i]
                    right = expression[i+1:]
                    
                    # Recursively compute the results for both parts
                    left_results = compute(left)
                    right_results = compute(right)
                    
                    # Combine the results from both sides using the operator
                    for l in left_results:
                        for r in right_results:
                            if expression[i] == '+':
                                result.append(l + r)
                            elif expression[i] == '-':
                                result.append(l - r)
                            else:  # expression[i] == '*'
                                result.append(l * r)
            
            # Save the result in the memoization dictionary and return it
            memo[expression] = result
            return result
        
        # Call the recursive function and return the result for the whole expression
        return compute(expression)
    
# Example Usage
solution = Solution()

# Test case 1
expression = "2-1-1"
print(solution.diffWaysToCompute(expression))  # Output: [0, 2]

# Test case 2
expression = "2*3-4*5"
print(solution.diffWaysToCompute(expression))  # Output: [-34, -14, -10, -10, 10]
