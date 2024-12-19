class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0  # To track the balance between 'L' and 'R'
        count = 0    # To count the number of balanced substrings
        
        # Iterate through the string
        for char in s:
            if char == 'L':
                balance += 1
            else:  # char == 'R'
                balance -= 1
            
            # If balance is zero, we found a balanced substring
            if balance == 0:
                count += 1
        
        return count
