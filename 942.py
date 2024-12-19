class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        low, high = 0, n
        result = []
        
        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            else:  # char == 'D'
                result.append(high)
                high -= 1
        
        # Add the last remaining number
        result.append(low)  # or high, as low == high at this point
        return result
