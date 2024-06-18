class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = list(s)
        n = len(s)

        for i in range(0, n, 2 * k):
            start = i
            end = min(i + k - 1, n - 1)

            while start < end:
                result[start], result[end] = result[end], result[start]
                start += 1
                end -= 1

        return ''.join(result)