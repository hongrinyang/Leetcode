class Solution:
    def lastRemaining(self, n: int) -> int:
        # Find the largest power of 2 less than or equal to n
        return n & ~(n - 1)

# Example Usage
solution = Solution()

# Test case 1
n = 9
print(solution.lastRemaining(n))  # Output: 6

# Test case 2
n = 1
print(solution.lastRemaining(n))  # Output: 1
