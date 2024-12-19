from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_permutation, used):
            if len(current_permutation) == len(nums):
                results.append(current_permutation[:])  # Append a copy of the current permutation
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue  # Skip already used numbers
                
                # Include nums[i] in the current permutation
                used[i] = True
                current_permutation.append(nums[i])
                
                # Recur
                backtrack(current_permutation, used)
                
                # Backtrack
                current_permutation.pop()  # Remove last element
                used[i] = False  # Mark it as unused

        results = []
        used = [False] * len(nums)  # Keep track of used numbers
        backtrack([], used)
        return results