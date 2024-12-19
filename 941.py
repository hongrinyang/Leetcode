class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        
        # Step 1: Check for the minimum length
        if n < 3:
            return False
        
        # Step 2: Find the peak, first find the increasing part
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # Step 3: Check if peak is not at the start or end
        if i == 0 or i == n - 1:
            return False
        
        # Step 4: Now check the decreasing part
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        # Step 5: If we reached the end, it's a valid mountain
        return i == n - 1
