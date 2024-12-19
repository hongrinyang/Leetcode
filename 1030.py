class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int):
        # List to store all coordinates
        result = []
        
        # Loop through all possible coordinates
        for r in range(rows):
            for c in range(cols):
                # Calculate the Manhattan distance
                distance = abs(r - rCenter) + abs(c - cCenter)
                result.append((r, c, distance))
        
        # Sort the coordinates by distance
        result.sort(key=lambda x: x[2])
        
        # Extract only the coordinates (ignoring the distance)
        return [[r, c] for r, c, _ in result]
