class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # There are 2^n subsets
        for subset_mask in range(1 << n):
            subset_xor = 0
            for i in range(n):
                if subset_mask & (1 << i):
                    subset_xor ^= nums[i]
            total_sum += subset_xor
        
        return total_sum

# Example usage:
solution = Solution()
print(solution.subsetXORSum([1, 3]))  # Output: 6
print(solution.subsetXORSum([5, 1, 6]))  # Output: 28
print(solution.subsetXORSum([3, 4, 5, 6, 7, 8]))  # Output: 480