class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        
        max_len = 1
        cur_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
        
        # Final check after loop ends
        max_len = max(max_len, cur_len)
        
        return max_len
