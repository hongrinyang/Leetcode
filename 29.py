class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define the 32-bit integer bounds
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle edge cases
        if dividend == 0:
            return 0
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        # Perform division using bit manipulation
        quotient = 0
        while dividend >= divisor:
            # Find the largest multiple of divisor using left shifts
            temp_divisor, num_shifts = divisor, 0
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_shifts += 1

            # Subtract the largest multiple and update the quotient
            dividend -= temp_divisor
            quotient += (1 << num_shifts)

        # Apply the sign
        if negative:
            quotient = -quotient

        # Clamp the result to 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))

