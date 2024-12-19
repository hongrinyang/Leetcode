class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Convert digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Check for overflow and clamp if necessary
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1

        return sign * result
