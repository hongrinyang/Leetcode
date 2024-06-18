from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [0] * n
        prev = float('-inf')
        
        # Forward pass to find distances to the closest 'c' on the left
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = abs(i - prev)
        
        prev = float('inf')
        
        # Backward pass to find distances to the closest 'c' on the right
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], abs(i - prev))
        
        return answer

# Example usage:
s = "loveleetcode"
c = "e"
solution = Solution()
print(solution.shortestToChar(s, c))  # Output: [3,2,1,0,1,0,0,1,2,2,1,0]

s = "aaab"
c = "b"
print(solution.shortestToChar(s, c))  # Output: [3,2,1,0]
