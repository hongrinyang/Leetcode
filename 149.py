from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        def get_slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:  # Vertical line
                return ('inf', 0)
            if dy == 0:  # Horizontal line
                return (0, 'inf')
            d = gcd(dx, dy)
            return (dy // d, dx // d)

        max_points = 0

        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicate = 1  # Count the current point as a duplicate

            for j in range(len(points)):
                if i == j:
                    continue
                if points[i] == points[j]:
                    duplicate += 1  # Count duplicate points
                else:
                    s = get_slope(points[i], points[j])
                    slopes[s] += 1

            # Calculate the maximum points passing through points[i]
            current_max = duplicate + max(slopes.values(), default=0)
            max_points = max(max_points, current_max)

        return max_points

# Example usage
solution = Solution()
points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
result = solution.maxPoints(points)
print(result)
