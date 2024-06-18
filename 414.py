class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = [float('-inf')] * 3

        for num in nums:
            if num in max_nums:
                continue
            if num > max_nums[0]:
                max_nums = [num, max_nums[0], max_nums[1]]
            elif num > max_nums[1]:
                max_nums = [max_nums[0], num, max_nums[1]]
            elif num > max_nums[2]:
                max_nums = [max_nums[0], max_nums[1], num]

        return max_nums[2] if float('-inf') not in max_nums else max_nums[0]