def perSquare(n):
    
    if n == 1:
        return 1
    
    p = int(sqrt(n))
    
    if p*p == n:
        return 1 

    sol = [n+10]*(n+1)
    sol[0] = 0
    
    for p in range(1, n+1):
        i = 1
        while i*i <= p:
            sol[p] = min(sol[p], 1+sol[p-i*i])
            i = i+1
        
    return sol[n]
    
   
class Solution:
    def numSquares(self, n: int) -> int:
        count = perSquare(n)
        return count