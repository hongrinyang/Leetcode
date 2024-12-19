class Solution:
    def sortArrayByParityII(self, nums):
        # Initialize pointers for even and odd indices
        even_index = 0
        odd_index = 1
        
        # Iterate through the array
        while even_index < len(nums) and odd_index < len(nums):
            # If even index has an odd number, swap it with the odd index
            if nums[even_index] % 2 != 0:
                # Swap the numbers at even_index and odd_index
                nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
                odd_index += 2  # Move to next odd index
            else:
                even_index += 2  # Move to next even index
        
        return nums
