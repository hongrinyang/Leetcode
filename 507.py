class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        total_sum = 1

        sqrt_n = int(num**0.5)
        for i in range(2, sqrt_n + 1):
            if num % i == 0:
                total_sum += i
                if i != num // i:
                    total_sum += num // i
        
        return total_sum == num