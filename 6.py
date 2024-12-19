class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is 1 or s is too short, return s as is
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize a list for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Place each character in the appropriate row
        for char in s:
            rows[current_row] += char
            # Change direction when reaching the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1
        
        # Combine rows to form the final string
        return ''.join(rows)
