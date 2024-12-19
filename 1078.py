class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        # Split the text into words
        words = text.split()
        result = []
        
        # Iterate over words, but we need at least two more words after the current one
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                # The third word is immediately after the second word
                result.append(words[i + 2])
        
        return result
