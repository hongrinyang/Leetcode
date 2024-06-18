class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)
        
        target = (total_alice + total_bob) // 2
        
        set_bob = set(bobSizes)
        
        for candy in aliceSizes:
            if (target - total_alice + candy) in set_bob:
                return [candy, target - total_alice + candy]