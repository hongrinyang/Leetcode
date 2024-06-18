class Solution:
    def moveZeroes(self, nums):
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                if i != non_zero_index:
                    nums[i] = 0
                non_zero_index += 1