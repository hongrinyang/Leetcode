class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        result = []
        carry = k
        i = len(num) - 1
        
        # Process the array from right to left
        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]  # Add the current digit
            result.append(carry % 10)  # Extract the current digit
            carry //= 10  # Carry over to the next place
            i -= 1
        
        # Reverse the result array to get the final number
        return result[::-1]
