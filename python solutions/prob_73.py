class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                
                if matrix[i][j] == 0:
                    
                    if matrix[i][0] =='-Inf':
                        matrix[i][0] == 2**31
                    elif matrix[i][0] != 2**31:
                        matrix[i][0] = 'Inf'
                        
                    if matrix[0][j] == 'Inf':
                        matrix[0][j] = 2**31
                        
                    elif matrix[0][j] != 2**31:
                        matrix[0][j] = '-Inf'
                        
                    if i == 0 and j == 0:
                        matrix[0][0] = 1 << 31                
                         
        print(matrix)
       
    
        for i in range(m):
            if matrix[i][0] == "Inf":
                matrix[i] = [0 if matrix[i][p] != "-Inf" else matrix[i][p] for p in range(n) ]
               
        
        print(matrix)
        
        for j in range(n):
            if matrix[0][j] == "-Inf":
                for x in matrix:
                    x[j] = 0
                    
        if matrix[0][0] == "Inf":
            matrix[0]  = [0 for p in range(n)]
       
        elif matrix[0][0] == "-Inf":
            for x in matrix:
                x[0] = 0
        elif matrix[0][0] == 2**31:
            matrix[0]  = [0 for p in range(n)]
            for x in matrix:
                x[0] = 0
            
            
        
                    
      
                