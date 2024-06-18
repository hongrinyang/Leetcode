class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Extract the column letter and row number
        column = coordinates[0]
        row = coordinates[1]
        
        # Convert column to a number (a=1, b=2, ..., h=8)
        column_num = ord(column) - ord('a') + 1
        # Convert row to an integer
        row_num = int(row)
        
        # Determine the color of the square
        return (column_num + row_num) % 2 == 1

# Example usage:
solution = Solution()
print(solution.squareIsWhite("a1"))  # Output: False
print(solution.squareIsWhite("h3"))  # Output: True
print(solution.squareIsWhite("c7"))  # Output: False
