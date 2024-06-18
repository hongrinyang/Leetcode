from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        
        # Initialize dp array
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Build dp array
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The result is the minimum of reaching the top from the last or second last step
        return min(dp[n-1], dp[n-2])
