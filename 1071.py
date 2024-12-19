import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Find the greatest common divisor of the lengths of str1 and str2
        gcd_length = math.gcd(len(str1), len(str2))
        
        # The candidate for the gcd string is the prefix of str1 of length gcd_length
        candidate = str1[:gcd_length]
        
        # Check if this candidate divides both str1 and str2
        if str1 == candidate * (len(str1) // len(candidate)) and str2 == candidate * (len(str2) // len(candidate)):
            return candidate
        else:
            return ""
