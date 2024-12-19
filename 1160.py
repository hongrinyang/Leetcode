from collections import Counter

class Solution:
    def countCharacters(self, words, chars):
        # Count the frequency of each character in chars
        chars_count = Counter(chars)
        total_length = 0
        
        # Check each word in words
        for word in words:
            word_count = Counter(word)
            
            # Check if each character in word can be formed from chars
            if all(word_count[char] <= chars_count[char] for char in word_count):
                total_length += len(word)
        
        return total_length
