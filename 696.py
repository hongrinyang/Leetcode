class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prevLength = 0
        curLength = 1  # Start with the first segment length
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curLength += 1
            else:
                count += min(prevLength, curLength)
                prevLength = curLength
                curLength = 1
        
        # Don't forget to add the last valid segment length
        count += min(prevLength, curLength)
        
        return count