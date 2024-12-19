class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Define mappings for numbers
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
                         "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                         "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            # Convert number less than 1000 to words
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n]
            elif n < 100:
                return tens[n // 10] + (" " + less_than_20[n % 10] if n % 10 != 0 else "")
            else:
                return less_than_20[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
        
        result = ""
        thousand_index = 0
        
        # Process each group of three digits
        while num > 0:
            if num % 1000 != 0:
                result = helper(num % 1000) + ("" if thousands[thousand_index] == "" else " " + thousands[thousand_index]) + (" " + result if result else "")
            num //= 1000
            thousand_index += 1
        
        return result.strip()

# Example Usage
solution = Solution()

# Test case 1
num = 123
print(solution.numberToWords(num))  # Output: "One Hundred Twenty Three"

# Test case 2
num = 12345
print(solution.numberToWords(num))  # Output: "Twelve Thousand Three Hundred Forty Five"

# Test case 3
num = 1234567
print(solution.numberToWords(num))  # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
