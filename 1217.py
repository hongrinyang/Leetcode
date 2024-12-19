class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        # Count how many chips are at even and odd positions
        even_count = 0
        odd_count = 0
        
        for pos in position:
            if pos % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        # The result is the minimum of moving all chips to an even position or to an odd position
        return min(even_count, odd_count)
