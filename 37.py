from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle in-place.
        """
        def is_valid(row: int, col: int, num: str) -> bool:
            # Check if the number is already in the row
            if num in board[row]:
                return False
            
            # Check if the number is already in the column
            for r in range(9):
                if board[r][col] == num:
                    return False
            
            # Check if the number is in the 3x3 box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            
            return True

        def solve() -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(i, j, num):
                                board[i][j] = num  # Place num
                                
                                if solve():  # Recursive call
                                    return True
                                
                                board[i][j] = '.'  # Backtrack
                        return False  # No valid number found, backtrack
            return True  # Puzzle is solved

        solve()
