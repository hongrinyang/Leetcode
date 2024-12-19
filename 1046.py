import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert stones into a max-heap (using negative values for max-heap behavior)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # Process until we have one or zero stones left
        while len(max_heap) > 1:
            # Pop the two largest stones (remember to negate them to get the original values)
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            
            if stone1 != stone2:
                # The new stone is the difference between the two
                heapq.heappush(max_heap, -(stone1 - stone2))
        
        # If there's a stone left, return its weight (negate to get the positive value)
        return -max_heap[0] if max_heap else 0
