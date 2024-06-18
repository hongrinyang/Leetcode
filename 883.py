from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_area = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        yz_area = sum(max(row) for row in grid)
        zx_area = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return xy_area + yz_area + zx_area