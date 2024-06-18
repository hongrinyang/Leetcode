class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize pointers for both strings
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        # Loop through both strings from the end to the beginning
        while i >= 0 or j >= 0 or carry:
            total_sum = carry
            
            if i >= 0:
                total_sum += int(a[i])
                i -= 1
            if j >= 0:
                total_sum += int(b[j])
                j -= 1
            
            # Compute the current digit and the new carry
            carry = total_sum // 2
            result.append(str(total_sum % 2))
        
        # The result is in reverse order, reverse it back
        return ''.join(result[::-1])
