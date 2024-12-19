class Solution:
    def trimMean(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Calculate the number of elements to remove
        n = len(arr)
        remove_count = n // 20  # 5% of n (n is guaranteed to be a multiple of 20)
        
        # Step 3: Remove the smallest and largest 5% elements
        remaining_arr = arr[remove_count:n-remove_count]
        
        # Step 4: Calculate and return the mean of the remaining elements
        return sum(remaining_arr) / len(remaining_arr)
