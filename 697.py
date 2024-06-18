from typing import List
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        left = {}
        right = {}
        max_freq = 0
        
        # Populate frequency and first/last occurrence information
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            freq[num] += 1
            max_freq = max(max_freq, freq[num])
        
        min_length = len(nums)
        
        # Find the smallest subarray with the maximum frequency elements
        for num in freq:
            if freq[num] == max_freq:
                min_length = min(min_length, right[num] - left[num] + 1)
        
        return min_length