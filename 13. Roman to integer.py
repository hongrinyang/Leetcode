class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to integers
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the string from right to left
        for char in reversed(s):
            current_value = roman_values[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
            
        return total

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))     # Output: 3
print(solution.romanToInt("LVIII"))   # Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994