class Solution:
    def prefixesDivBy5(self, nums):
        result = []
        current_mod = 0
        
        # Traverse through each element of nums
        for num in nums:
            # Update the current value of xi mod 5
            current_mod = (current_mod * 2 + num) % 5
            
            # Check if current_mod is divisible by 5
            result.append(current_mod == 0)
        
        return result

# Example usage:
solution = Solution()

# Test case 1
nums1 = [0, 1, 1]
print(solution.prefixesDivBy5(nums1))  # Output: [True, False, False]

# Test case 2
nums2 = [1, 1, 1]
print(solution.prefixesDivBy5(nums2))  # Output: [False, False, False]
