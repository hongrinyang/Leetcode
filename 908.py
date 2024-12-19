class Solution:
    def smallestRangeI(self, nums, k):
        # Find the current minimum and maximum in the array
        min_val = min(nums)
        max_val = max(nums)
        
        # The minimum score after the operation would be max_val - min_val - 2 * k
        # But it cannot be negative, so we return the maximum of 0 and this result.
        return max(0, max_val - min_val - 2 * k)
