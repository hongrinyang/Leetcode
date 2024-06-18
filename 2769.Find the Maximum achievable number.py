class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t

# Example usage
solution = Solution()
print(solution.theMaximumAchievableX(4, 1))  # Output: 6
print(solution.theMaximumAchievableX(3, 2))  # Output: 7
