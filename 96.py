class Solution:
    def numTrees(self, n):
        # Initialize an array to store Catalan numbers
        catalan = [0] * (n + 1)

        # Base cases
        catalan[0] = 1
        catalan[1] = 1

        # Compute Catalan numbers using dynamic programming
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        return catalan[n]

# Example usage
solution = Solution()
n = 3
result = solution.numTrees(n)
print(result)
