from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Calculate expected sums
        sum_n = n * (n + 1) // 2
        sum_squares_n = n * (n + 1) * (2 * n + 1) // 6
        
        # Calculate actual sums
        sum_nums = sum(nums)
        sum_squares_nums = sum(x * x for x in nums)
        
        # Calculate the differences
        diff_sum = sum_n - sum_nums  # missing - duplicate
        diff_squares = sum_squares_n - sum_squares_nums  # missing^2 - duplicate^2
        
        # From the equations:
        # missing - duplicate = diff_sum
        # missing^2 - duplicate^2 = diff_squares
        # We know that (missing + duplicate) = diff_squares / diff_sum
        sum_m_d = diff_squares // diff_sum  # missing + duplicate
        
        # Now solve for missing and duplicate
        missing = (diff_sum + sum_m_d) // 2
        duplicate = sum_m_d - missing
        
        return [duplicate, missing]