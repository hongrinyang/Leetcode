class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        num_unique_types = len(set(candyType))
        max_types_to_eat = min(num_unique_types, len(candyType) // 2)
        return max_types_to_eat
