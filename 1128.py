from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = defaultdict(int)  # Dictionary to store the frequency of normalized dominoes
        result = 0
        
        # Iterate over each domino
        for domino in dominoes:
            # Sort the domino to normalize it
            normalized = tuple(sorted(domino))
            count[normalized] += 1
        
        # Now, calculate the number of pairs for each group of equivalent dominoes
        for num in count.values():
            if num > 1:
                result += (num * (num - 1)) // 2  # Combinatorial count of pairs
        
        return result
