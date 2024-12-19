class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)  # dp[i] will be True if the player whose turn it is can win at state i
        
        # Base case: dp[1] = False, as the player cannot make a move and loses.
        dp[1] = False
        
        # Fill the dp array for all states from 2 to n
        for i in range(2, n + 1):
            # Check all divisors of i (0 < x < i and i % x == 0)
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break  # No need to check further if we found a winning move
        
        # The result for Alice starting with n is dp[n]
        return dp[n]
