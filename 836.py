from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x1_, y1_, x2_, y2_ = rec2

        if x2 <= x1_ or x2_ <= x1:
            return False

        if y2 <= y1_ or y2_ <= y1:
            return False

        return True
