from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]):
            if target == 0:
                result.append(path.copy())  # Found a valid combination
                return
            if target < 0:
                return  # Exceeded target, no need to continue
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include the candidate and continue searching
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)  # Move to the next index
                path.pop()  # Backtrack
        
        result = []
        candidates.sort()  # Sort to handle duplicates
        backtrack(0, target, [])
        return result
