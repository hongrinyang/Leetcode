class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial

        # Create a list of numbers to pick from
        numbers = list(range(1, n + 1))
        # Adjust k to be zero-indexed
        k -= 1
        result = []

        # Iterate to build the permutation
        for i in range(n, 0, -1):
            # Determine the size of each group
            fact = factorial(i - 1)
            # Find the index of the current number
            index = k // fact
            # Append the selected number to the result
            result.append(str(numbers[index]))
            # Remove the used number
            numbers.pop(index)
            # Update k for the next iteration
            k %= fact

        return ''.join(result)
