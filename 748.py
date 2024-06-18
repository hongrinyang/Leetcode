class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: Normalize licensePlate
        lp_chars = [c.lower() for c in licensePlate if c.isalpha()]
        
        # Step 2: Count frequency of characters in licensePlate
        lp_char_count = {}
        for char in lp_chars:
            if char in lp_char_count:
                lp_char_count[char] += 1
            else:
                lp_char_count[char] = 1
        
        # Step 3: Find the shortest completing word
        shortest_word = None
        for word in words:
            # Create a copy of lp_char_count to work with
            remaining_chars = lp_char_count.copy()
            
            # Check if word contains at least the required characters
            for char in word:
                if char.lower() in remaining_chars:
                    remaining_chars[char.lower()] -= 1
                    if remaining_chars[char.lower()] == 0:
                        del remaining_chars[char.lower()]
                
                # If all required characters are found
                if not remaining_chars:
                    if shortest_word is None or len(word) < len(shortest_word):
                        shortest_word = word
                    break
        
        return shortest_word
