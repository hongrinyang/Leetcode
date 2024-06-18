from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        result = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key in count:
            if count[key] > 1:
                result += count[key] * (count[key] - 1) // 2
        return result

# Example usage
solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # Output: 4
print(solution.numIdenticalPairs([1, 1, 1, 1]))        # Output: 6
print(solution.numIdenticalPairs([1, 2, 3]))           # Output: 0
