import math

class Solution:
    def constructRectangle(self, area: int) -> [int]:
        for W in range(int(math.sqrt(area)), 0, -1):
            if area % W == 0:
                L = area // W
                return [L, W]