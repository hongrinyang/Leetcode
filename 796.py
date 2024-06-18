class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths are different, immediate return False
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself to form all possible rotations
        s_double = s + s
        
        # Check if goal is a substring of s_double
        if goal in s_double:
            return True
        else:
            return False
