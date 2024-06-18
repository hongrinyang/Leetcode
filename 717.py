from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                if i == len(bits):
                    return True
            elif bits[i] == 1:
                i += 2
                if i == len(bits):
                    return False
        return False