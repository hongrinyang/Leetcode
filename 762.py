class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        def count_set_bits(n):
            return bin(n).count('1')
        
        prime_count = 0
        
        for num in range(left, right + 1):
            set_bits = count_set_bits(num)
            if is_prime(set_bits):
                prime_count += 1
        
        return prime_count
