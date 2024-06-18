class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]  # Get binary representation of n without the '0b' prefix
        max_distance = 0
        last_index = None
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if last_index is not None:
                    max_distance = max(max_distance, i - last_index)
                last_index = i
        
        return max_distance