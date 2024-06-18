class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result += (ord(columnTitle[len(columnTitle) - i - 1]) - ord('A') + 1) * (26 ** i)
        return result