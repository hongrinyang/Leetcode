class Solution:
    def soupServings(self, n):
        if n > 4800:
            return 1.0  # Approximation for large n

        # Convert n to units of 25 ml
        n = (n + 24) // 25

        memo = {}

        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5  # Both A and B empty at the same time
            if a <= 0:
                return 1.0  # A is empty first
            if b <= 0:
                return 0.0  # B is empty first

            if (a, b) in memo:
                return memo[(a, b)]

            memo[(a, b)] = 0.25 * (
                dfs(a - 4, b) +  # Serve 100 ml of A, 0 ml of B
                dfs(a - 3, b - 1) +  # Serve 75 ml of A, 25 ml of B
                dfs(a - 2, b - 2) +  # Serve 50 ml of A, 50 ml of B
                dfs(a - 1, b - 3)    # Serve 25 ml of A, 75 ml of B
            )
            return memo[(a, b)]

        return dfs(n, n)

# Example usage
solution = Solution()
n = 50
result = solution.soupServings(n)
print(result)
