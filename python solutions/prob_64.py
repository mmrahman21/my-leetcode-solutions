import numpy as np

sol = {}

def minPath(row, col, grid):
    maxRow = len(grid) 
    maxCol = len(grid[0]) 
    
    if (row, col) in sol.keys():
        return sol[(row, col)]
    
    elif row == maxRow - 1 and col == maxCol - 1:
        sol[(row, col)] = grid[row, col]
        return sol[(row, col)]
    
    elif row == maxRow - 1:
        sol[(row, col)] = sum(grid[row, col:maxCol])
        return sol[(row, col)]
    
    elif col == maxCol - 1:
        sol[(row, col)] = sum(grid[row:maxRow , col])
        return sol[(row, col)]
    else:
        sol[(row, col)] = grid[row, col] + min(minPath(row+1, col, grid), minPath(row, col+1, grid))
        return sol[(row, col)]
    

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        grid = np.array(grid)
        
        result = minPath(0, 0, grid)
      
        sol.clear()
        
        return result
        
        