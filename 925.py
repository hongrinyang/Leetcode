class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            # If the characters match, move both pointers
            if i < len(name) and name[i] == typed[j]:
                i += 1
            # If not, ensure it's a long press (i.e., typed[j] is the same as typed[j-1])
            elif j > 0 and typed[j] == typed[j-1]:
                pass  # Just move `j` forward if it's a long press
            else:
                return False  # Otherwise, return False as the characters don't match
            
            # Always move `j` forward
            j += 1
        
        # Ensure that we have processed all characters of `name`
        return i == len(name)
