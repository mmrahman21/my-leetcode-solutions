sol = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            sol[n] = 1
            return sol[n]
        elif n == 2:
            sol[n] = 2
            return sol[n]
        
        else:
            if n in sol.keys():
                return sol[n]
            else:
                sol[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                return sol[n]
        
print(Solution().climbStairs(40))