class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        max_num = -1
        max_index = -1
        
        # Find the largest element and its index
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_index = i
        
        # Verify the condition
        for i, num in enumerate(nums):
            if i != max_index and max_num < 2 * num:
                return -1
        
        return max_index
