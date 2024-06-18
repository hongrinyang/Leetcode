class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Use two pointers
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

# Example usage
solution = Solution()
nums1 = [1, 1, 2]
print(solution.removeDuplicates(nums1))  # Output: 2, nums1 = [1, 2, _]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums2))  # Output: 5, nums2 = [0, 1, 2, 3, 4, _, _, _, _, _]
