class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        i, j = 0, 0
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        result = [matrix[0][0]]
        
        matrix[0][0] = -101
        
        flag = "right"
        
        count = 1
        
        while count < m*n:
            
            if flag == "right":
                
                if j + 1 < n and matrix[i][j+1] != -101:
                    result.append(matrix[i][j+1])
                    matrix[i][j+1] = -101
                    count += 1
                    j += 1
                else:
                    flag = "down"
            elif flag == "down":
                
                if i + 1 < m and matrix[i+1][j] != -101:
                    result.append(matrix[i+1][j])
                    matrix[i+1][j] = -101
                    i += 1
                    count += 1
                else:
                    flag = "left"
            elif flag == "left":
                if j - 1 >=0 and matrix[i][j-1] != -101:
                    result.append(matrix[i][j-1])
                    matrix[i][j-1] = -101
                    j -= 1
                    count += 1
                else:
                    flag = "up"
            elif flag == "up":
                if i - 1 >= 0 and matrix[i-1][j] != -101:
                    result.append(matrix[i-1][j])
                    matrix[i-1][j] = -101
                    i -= 1
                    count += 1
                else:
                    flag = "right"
                    
        return result
                
                
        