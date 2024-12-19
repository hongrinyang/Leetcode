class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Initialize pointers and result array
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1  # Position to insert squared values
        
        # Two-pointer approach
        while left <= right:
            left_val, right_val = abs(nums[left]), abs(nums[right])
            if left_val > right_val:
                result[pos] = left_val ** 2
                left += 1
            else:
                result[pos] = right_val ** 2
                right -= 1
            pos -= 1
        
        return result
