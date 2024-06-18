class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_col = n
        
        # Iterate through each operation
        for op in ops:
            min_row = min(min_row, op[0])
            min_col = min(min_col, op[1])
        
        # Return the product of min_row and min_col
        return min_row * min_col