class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        
        elif n==1:
            return x
        
        else:
        
            half = self.myPow(x, abs(n) // 2)
            rem = self.myPow(x, abs(n) % 2)
            sol = half*half*rem
        
        if n < 0:
            return 1/sol
        else:
            return sol

print(Solution().myPow(2.0, -2))