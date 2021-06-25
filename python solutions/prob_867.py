class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        res = []
        
        for i in range(n):
            row = []
            
            for j in range(m):
                row.append(matrix[j][i])
            
            res.append(row)
        
        return res