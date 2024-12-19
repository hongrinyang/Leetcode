class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Step 1: Create the expected array by sorting the heights
        expected = sorted(heights)
        
        # Step 2: Compare the heights with the expected array
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        
        # Step 3: Return the result
        return count
