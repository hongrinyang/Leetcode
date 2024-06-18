from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            # Flip each row horizontally
            row.reverse()
            # Invert each element in the row
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return image

# Example usage:
image1 = [[1,1,0],[1,0,1],[0,0,0]]
image2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

solution = Solution()
print(solution.flipAndInvertImage(image1))  # Output: [[1,0,0],[0,1,0],[1,1,1]]
print(solution.flipAndInvertImage(image2))  # Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
