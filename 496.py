class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            stack.append(num)

        result = []
        for num in nums1:
            result.append(next_greater[num])
        
        return result