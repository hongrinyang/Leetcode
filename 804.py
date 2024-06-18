class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Define the Morse code mapping
        morse_mapping = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", 
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", 
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        
        # Create a set to store unique Morse code transformations
        transformations = set()
        
        # Iterate through each word in the list
        for word in words:
            morse_code = []
            # Transform each character in the word to its Morse code
            for char in word:
                morse_code.append(morse_mapping[ord(char) - ord('a')])
            # Join the list of Morse code characters into a single string
            morse_str = ''.join(morse_code)
            # Add the Morse code string to the set (automatically handles uniqueness)
            transformations.add(morse_str)
        
        # Return the number of unique transformations
        return len(transformations)

