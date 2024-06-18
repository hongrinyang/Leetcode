from typing import List
from collections import defaultdict
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Normalize the paragraph by converting to lowercase and replacing punctuation with spaces
        normalized_str = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        words = normalized_str.split()
        
        # Initialize the frequency dictionary and the set of banned words
        word_count = defaultdict(int)
        banned_set = set(banned)
        
        # Count the frequency of each word that is not banned
        for word in words:
            if word not in banned_set:
                word_count[word] += 1
        
        # Find the word with the maximum frequency
        max_freq = 0
        most_common_word = ''
        for word, freq in word_count.items():
            if freq > max_freq:
                max_freq = freq
                most_common_word = word
        
        return most_common_word

# Example usage:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
solution = Solution()
print(solution.mostCommonWord(paragraph, banned))  # Output: "ball"
