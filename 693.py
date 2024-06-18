class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = n & 1  # Get the LSB (least significant bit)
        n >>= 1  # Right shift to move to the next bit
        
        while n > 0:
            current_bit = n & 1
            if current_bit == prev_bit:
                return False
            prev_bit = current_bit
            n >>= 1
        
        return True
