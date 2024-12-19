class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the position of the rook
        rook_row, rook_col = -1, -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break
            if rook_row != -1:
                break

        # Helper to count pawns in a direction
        def count_pawns(dx, dy):
            x, y = rook_row, rook_col
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if not (0 <= x < 8 and 0 <= y < 8):
                    break
                if board[x][y] == 'B':  # Stop at a bishop
                    break
                if board[x][y] == 'p':  # Pawn found
                    return 1
            return 0

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total_pawns = sum(count_pawns(dx, dy) for dx, dy in directions)
        return total_pawns
