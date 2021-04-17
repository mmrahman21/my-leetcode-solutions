class Solution:
    def fib(self, n: int) -> int:
        F = [0, 1]
        
        i = 2
        
        while i<=n:
            F.append(F[-1] + F[-2])
            i += 1
        
        return F[n]
        