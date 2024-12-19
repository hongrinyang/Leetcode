from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            
            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # Target is in the left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # If the target is not found, return -1
        return -1
