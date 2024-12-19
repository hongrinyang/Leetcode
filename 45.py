from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # We don't need to jump from the last element
            farthest = max(farthest, i + nums[i])  # Update the farthest point we can reach
            
            # If we reach the end of the current jump range
            if i == current_end:
                jumps += 1  # Increment the jump count
                current_end = farthest  # Update the current end to the farthest point
            
            # If the current end is at or beyond the last index, we can return
            if current_end >= n - 1:
                break
            
        return jumps
