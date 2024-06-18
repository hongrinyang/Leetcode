class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip the string to remove trailing spaces
        s = s.strip()
        # Split the string by spaces to get all words
        words = s.split()
        # Return the length of the last word
        return len(words[-1])
