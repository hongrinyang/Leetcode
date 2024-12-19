from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Step 1: Count the frequency of each element in arr1
        count = Counter(arr1)
        
        # Step 2: Create the result list by placing elements of arr2 first
        result = []
        
        # Append elements in the order of arr2
        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0  # Clear the count for the number already added
        
        # Step 3: Append the remaining elements in sorted order
        remaining_elements = []
        for num in count:
            if count[num] > 0:
                remaining_elements.extend([num] * count[num])
        
        # Sort the remaining elements
        remaining_elements.sort()
        
        # Final result
        return result + remaining_elements
