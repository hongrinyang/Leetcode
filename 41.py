from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Place each number in its right position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        
        # Step 2: Identify the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1  # If all numbers are in place, return n + 1
