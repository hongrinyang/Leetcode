class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        # Find the mask (all bits set to 1 with the same length as n)
        length = n.bit_length()  # Number of bits in binary representation of n
        mask = (1 << length) - 1  # Create mask with all 1's of the same length
        return n ^ mask  # XOR with the mask to flip bits
