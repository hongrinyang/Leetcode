from itertools import combinations
from collections import Counter
from math import comb

class Solution:
    def getProbability(self, balls):
        # Total number of balls
        n = sum(balls) // 2  # Since total number of balls is 2n
        
        # Generate a list of balls represented by their color
        all_balls = []
        for i, count in enumerate(balls):
            all_balls.extend([i] * count)
        
        # Generate all possible ways to split the balls into two groups of size n
        total_ways = comb(len(all_balls), n)
        
        # Count valid configurations where both boxes have the same number of distinct colors
        valid_ways = 0
        
        # Generate all combinations of n balls for the first box
        for comb1 in combinations(all_balls, n):
            comb1 = Counter(comb1)  # Count the occurrence of each color in box 1
            comb2 = Counter(all_balls) - comb1  # The remaining balls go to box 2
            
            # Check if both boxes have the same number of distinct colors
            if len(comb1) == len(comb2):
                valid_ways += 1
        
        # Probability of the two boxes having the same number of distinct colors
        return valid_ways / total_ways

# Example Usage
solution = Solution()

# Test case 1
balls = [1, 1]
print(solution.getProbability(balls))  # Expected: 1.00000

# Test case 2
balls = [2, 1, 1]
print(solution.getProbability(balls))  # Expected: 0.66667

# Test case 3
balls = [1, 2, 1, 2]
print(solution.getProbability(balls))  # Expected: 0.60000
