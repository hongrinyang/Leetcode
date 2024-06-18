class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = {}
        mapped_chars = set()
        
        for char_s, char_t in zip(s, t):
            if char_s in char_map:
                if char_map[char_s] != char_t:
                    return False
            else:
                if char_t in mapped_chars:
                    return False
                char_map[char_s] = char_t
                mapped_chars.add(char_t)
        
        return True