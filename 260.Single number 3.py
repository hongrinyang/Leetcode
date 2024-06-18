class Solution:
    def singleNumber(self, nums):
        xor_result = 0
        for num in nums:
            xor_result ^= num

        mask = 1
        while xor_result & mask == 0:
            mask <<= 1

        num1, num2 = 0, 0
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

# Example usage
solution = Solution()
print(solution.singleNumber([1, 2, 1, 3, 2, 5]))  # Output: [3, 5]
print(solution.singleNumber([-1, 0]))             # Output: [-1, 0]
print(solution.singleNumber([0, 1]))              # Output: [1, 0]
