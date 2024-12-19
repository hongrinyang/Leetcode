from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')  # Initialize closest sum with an infinitely large value

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Check if the current sum is closer to the target than the closest sum found so far
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers based on the comparison with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # If exact match, return immediately
        
        return closest_sum
