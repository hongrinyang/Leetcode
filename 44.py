class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # DP table where dp[i][j] means s[0...i-1] matches p[0...j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: both string and pattern are empty
        dp[0][0] = True
        
        # Initialize first row (when s is empty and p is a sequence of '*'s)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]  # Match single character
                elif p[j - 1] == '*':
                    # '*' matches empty sequence or one or more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[m][n]
