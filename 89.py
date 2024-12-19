class Solution:
    def grayCode(self, n):
        # Base case: 1-bit Gray code
        if n == 1:
            return [0, 1]

        # Recursive step: Generate (n-1)-bit Gray code
        smaller_gray = self.grayCode(n - 1)

        # Add 0 to the front of the original sequence
        with_zero = smaller_gray

        # Add 1 to the front of the reversed sequence
        with_one = [(1 << (n - 1)) | x for x in reversed(smaller_gray)]

        # Combine the two sequences
        return with_zero + with_one

# Example usage
solution = Solution()
n = 2
result = solution.grayCode(n)
print(result)
