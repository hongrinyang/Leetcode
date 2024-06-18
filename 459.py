class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_s = (s + s)[1:-1]
        return s in doubled_s
