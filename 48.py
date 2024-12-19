class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotates the input matrix by 90 degrees clockwise in-place.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
