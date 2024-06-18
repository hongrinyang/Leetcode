class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(c ** 0.5)

        while a <= b:
            total = a * a + b * b
            if total == c:
                return True
            elif total < c:
                a += 1
            else:
                b -= 1

        return False