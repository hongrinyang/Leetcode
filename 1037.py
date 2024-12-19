class Solution:
    def isBoomerang(self, points):
        # Check if the points are distinct
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        # Calculate the determinant (area condition)
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        determinant = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        
        # If determinant is non-zero, points are not collinear
        return determinant != 0
