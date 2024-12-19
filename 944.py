class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        # Number of columns is the length of each string (since all strings have the same length)
        num_columns = len(strs[0])
        
        # Variable to count the number of unsorted columns
        deletions = 0
        
        # Iterate over each column
        for j in range(num_columns):
            # Check if the column is sorted
            for i in range(1, len(strs)):
                if strs[i][j] < strs[i - 1][j]:
                    deletions += 1
                    break  # No need to check further for this column
                
        return deletions
