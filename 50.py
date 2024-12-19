class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_product = x

        while n > 0:
            # If n is odd, multiply the result by the current product
            if n % 2 == 1:
                result *= current_product

            # Square the current product for the next iteration
            current_product *= current_product
            # Halve n
            n //= 2

        return result
