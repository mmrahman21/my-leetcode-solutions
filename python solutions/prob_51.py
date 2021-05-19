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
                c = sol[:]
                solutions.append(c)
               
            else:
                NQueen(k+1, n)
                           

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
       
        global sol
        sol = [-1 for _ in range(n)]
        
        NQueen(0, n)
        
        formatted_solutions = []
        
        for item in solutions:
            new_sol = []
            for row in item:
                val = ""
                for q in range(n):
                    if q == row:
                        val +="Q"
                    else:
                        val +='.'
                new_sol.append(val)
                
            formatted_solutions.append(new_sol)
        
        sol.clear()
        solutions.clear()
        
        return formatted_solutions
            
                
                    
                
            
                   