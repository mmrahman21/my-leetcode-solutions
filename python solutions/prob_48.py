class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        for i in range(n // 2):
            for j in range(i, n-1-i):
                
                # It can be improved with just re-ordering of the swapping operations
                
                temp = matrix[j][n-1-i] 
                matrix[j][n-1-i] = matrix[i][j]
                temp2 = matrix[n-1-i][n-1-j] 
                matrix[n-1-i][n-1-j] = temp
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i] = temp2
                matrix[i][j] = temp
                
                
        print(matrix)
        