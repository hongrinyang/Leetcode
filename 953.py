class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Create a map of each character in the alien order to its index
        alien_order = {ch: i for i, ch in enumerate(order)}
        
        # Function to compare two words based on the alien alphabet order
        def is_sorted(word1, word2):
            # Compare character by character
            for i in range(min(len(word1), len(word2))):
                if alien_order[word1[i]] < alien_order[word2[i]]:
                    return True
                elif alien_order[word1[i]] > alien_order[word2[i]]:
                    return False
            # If the words are the same up to the length of the shortest word,
            # the shorter word should come first
            return len(word1) <= len(word2)
        
        # Compare each pair of consecutive words
        for i in range(1, len(words)):
            if not is_sorted(words[i-1], words[i]):
                return False
        
        return True
