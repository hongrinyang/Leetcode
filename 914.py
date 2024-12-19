from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        # Count the frequency of each card
        count = Counter(deck)
        
        # Get the frequencies of the cards
        freq_values = list(count.values())
        
        # Compute the GCD of all the frequencies
        overall_gcd = reduce(gcd, freq_values)
        
        # If GCD of all frequencies is greater than 1, return True, else return False
        return overall_gcd > 1
