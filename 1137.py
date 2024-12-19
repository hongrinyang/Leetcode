class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # Initialize the first three values of the Tribonacci sequence
        t0, t1, t2 = 0, 1, 1
        
        # Calculate the Tribonacci values for n >= 3
        for i in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next
        
        return t2  # t2 will hold the value of Tn after the loop