from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize common frequency using the first word
        common_freq = Counter(words[0])

        # Update common_freq for every subsequent word
        for word in words[1:]:
            word_freq = Counter(word)
            for char in common_freq.keys():
                if char in word_freq:
                    common_freq[char] = min(common_freq[char], word_freq[char])
                else:
                    common_freq[char] = 0

        # Build the result list from the common frequencies
        result = []
        for char, freq in common_freq.items():
            result.extend([char] * freq)

        return result
