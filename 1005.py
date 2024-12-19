class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Flip negative numbers
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        
        # Step 3: Handle remaining k
        if k % 2 == 1:
            # Flip the smallest absolute value
            nums.sort()
            nums[0] = -nums[0]
        
        # Step 4: Compute the sum
        return sum(nums)
