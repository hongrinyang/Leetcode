import random

def rand7():
    return random.randint(1, 7)

class Solution:
    def rand10(self):
        while True:
            # Generate a number in the range [1, 49] using two rand7() calls
            row = rand7()
            col = rand7()
            index = (row - 1) * 7 + col

            # Accept numbers in the range [1, 40] and reject others
            if index <= 40:
                return 1 + (index - 1) % 10

# Example usage
solution = Solution()
result = [solution.rand10() for _ in range(10)]
print(result)
