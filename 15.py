from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate elements for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Move left and right pointers to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
