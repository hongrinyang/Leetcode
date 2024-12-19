class Solution:
    def intToRoman(self, num: int) -> str:
        # Define Roman numeral symbols and values
        roman_symbols = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]
        
        result = ""
        
        # Iterate through the Roman numeral values and symbols
        for symbol, value in roman_symbols:
            while num >= value:
                result += symbol  # Append the Roman numeral symbol
                num -= value  # Subtract the corresponding value
        
        return result
