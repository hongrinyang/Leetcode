class Solution:
    def duplicateZeros(self, arr):
        # Count the number of zeros in the array
        zero_count = arr.count(0)
        
        # Length of the array
        n = len(arr)
        
        # Traverse the array from the end to the beginning
        for i in range(n - 1, -1, -1):
            if i + zero_count < n:
                arr[i + zero_count] = arr[i]
            
            # If the current element is zero, duplicate it
            if arr[i] == 0:
                zero_count -= 1
                if i + zero_count < n:
                    arr[i + zero_count] = 0
