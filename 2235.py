class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.sum(12, 5))   # Output: 17
    print(solution.sum(-10, 4))  # Output: -6