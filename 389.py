from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = defaultdict(int)
        
        for char in s:
            char_count[char] += 1
        
        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return char