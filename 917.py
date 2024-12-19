class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Step 1: Extract all the English letters into a list
        letters = [ch for ch in s if ch.isalpha()]
        
        # Step 2: Reverse the list of letters
        letters.reverse()
        
        # Step 3: Rebuild the string
        result = []
        for ch in s:
            if ch.isalpha():
                # Replace the current letter with the reversed one
                result.append(letters.pop(0))
            else:
                # Keep the non-alphabet character as it is
                result.append(ch)
        
        # Convert the list back to a string
        return ''.join(result)
