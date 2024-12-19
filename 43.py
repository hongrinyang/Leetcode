class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle the edge case where one of the numbers is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize the result array
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Perform multiplication digit by digit
        for i in range(m - 1, -1, -1):  # Start from the least significant digit of num1
            for j in range(n - 1, -1, -1):  # Start from the least significant digit of num2
                # Multiply the current digits
                product = (int(num1[i]) * int(num2[j]))
                # Determine positions in the result array
                pos1, pos2 = i + j, i + j + 1
                # Add the product to the corresponding position
                total = product + result[pos2]
                result[pos2] = total % 10  # Update the current position
                result[pos1] += total // 10  # Carry over
                
        # Convert the result array to a string
        result_str = ''.join(map(str, result))
        # Remove leading zeros
        return result_str.lstrip("0")
