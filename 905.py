class Solution:
    def sortArrayByParity(self, nums):
        # Create two lists to hold even and odd numbers
        even_nums = []
        odd_nums = []
        
        # Distribute the numbers into even and odd lists
        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)
        
        # Concatenate even and odd lists
        return even_nums + odd_nums
