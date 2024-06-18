from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize the sum of the first 'k' elements
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Slide the window from the start of the array to the end
        for i in range(k, len(nums)):
            # Update the sum by adding the next element and subtracting the first element of the previous window
            current_sum += nums[i] - nums[i - k]
            # Update the max_sum if the current_sum is larger
            max_sum = max(max_sum, current_sum)

        # Return the maximum average
        return max_sum / k