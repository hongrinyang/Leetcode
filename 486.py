from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # dp[i][j] will store the maximum score difference Player 1 can achieve over Player 2
        dp = [[0] * n for _ in range(n)]
        
        # Base case: when there is only one number, Player 1 takes it
        for i in range(n):
            dp[i][i] = nums[i]
        
        # Fill the dp table for subarrays of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        # If dp[0][n-1] >= 0, Player 1 can win or tie (since they start first)
        return dp[0][n - 1] >= 0

# Example Usage
solution = Solution()

# Test case 1
nums = [1, 5, 2]
print(solution.predictTheWinner(nums))  # Output: False

# Test case 2
nums = [1, 5, 233, 7]
print(solution.predictTheWinner(nums))  # Output: True
