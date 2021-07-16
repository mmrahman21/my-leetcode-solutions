solutions = []
sol = []

def place(k, i):
    for j in range(0, k):
        if sol[j] == i or abs(sol[j] - i) == abs(j - k):
            return False
    return True


def NQueen(k, n):
    for i in range(n):
        if place(k, i):
            sol[k] = i
            
            if k == n - 1:
                solutions.append(sol[:])
            else:
                NQueen(k+1, n)
    
                
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        global sol
        sol = [-1 for _ in range(n)]
        
        NQueen(0, n)
        
        res = len(solutions)
        
        
        solutions.clear()
        sol.clear()
        
        return res
        