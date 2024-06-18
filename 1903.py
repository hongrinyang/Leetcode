class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        
        # Iterate through the string from right to left
        for i in range(n - 1, -1, -1):
            # Check if the last digit is odd
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        
        # If no odd number is found, return an empty string
        return ""

