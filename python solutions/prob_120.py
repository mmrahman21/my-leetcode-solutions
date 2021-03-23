solution = {}
class Solution:
    def findminTotal(self, triangle, root_row, root_col):
        if len(triangle) == root_row + 1:
            return triangle[root_row][root_col]
        
        else:
            # triangle1 = [triangle[i][0:i] for i in range(root_row + 1, len(triangle))]
            # triangle2 = [triangle[i][1:] for i in range(root_row + 1, len(triangle))]
            t = (root_row, root_col)
            if t in solution.keys():
                return solution[t]
            
            solution[t] = triangle[root_row][root_col]+min(self.findminTotal(triangle, root_row + 1, root_col), self.findminTotal(triangle, root_row + 1, root_col + 1))
            
            return solution[t]
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sol = self.findminTotal(triangle, 0, 0)
        solution.clear()
        return sol
        
        
        