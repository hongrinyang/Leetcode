from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]):
            # If the remaining target is zero, we found a valid combination
            if target == 0:
                result.append(path)
                return
            # If the remaining target is negative, no need to continue
            if target < 0:
                return
            
            # Iterate through candidates starting from 'start'
            for i in range(start, len(candidates)):
                # Include the candidate and continue searching
                backtrack(i, target - candidates[i], path + [candidates[i]])
        
        result = []
        backtrack(0, target, [])
        return result
