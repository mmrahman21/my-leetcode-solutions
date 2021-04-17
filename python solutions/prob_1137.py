class Solution:
    def tribonacci(self, n: int) -> int:
        
        F = [0, 1, 1]
        
        i = 3
        
        while i <= n:
            F.append(F[-1] + F[-2] + F[-3])
            i += 1
        
        return F[n]
        
        