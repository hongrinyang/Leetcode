class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        place = 1  # Start with the ones place
        
        while place <= n:
            higher = n // (place * 10)  # Digits to the left of the current place
            current = (n // place) % 10  # The current digit
            lower = n % place  # Digits to the right of the current place
            
            # Counting the number of '1's at the current digit place
            if current == 0:
                count += higher * place
            elif current == 1:
                count += higher * place + lower + 1
            else:
                count += (higher + 1) * place
            
            place *= 10  # Move to the next higher place (tens, hundreds, etc.)
        
        return count
