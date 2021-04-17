class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        
        i, j = 0, 0
        
        res[i][j] = 1
        
        count = 2
        
        flag = "right"
        
        while count <= n*n:
            
            if flag == "right":
                
                if j + 1 < n and res[i][j+1] == 0:
                    res[i][j+1] = count
                    j += 1
                    count += 1
                else:
                    flag = "down"
            
                    
            elif flag == "down":
            
                if i+1 < n and res[i+1][j] ==0:
                    res[i+1][j] = count
                    i += 1
                    count += 1
                else:
                    flag = "left"
                    
                    
            elif flag == "left":
                
                if j - 1 >= 0 and res[i][j - 1] ==0:
                    res[i][j - 1] = count
                    j -= 1
                    count += 1
                else:
                    flag = "up"
            elif flag == "up":
                
                if i - 1 >= 0 and res[i-1][j] == 0:
                    res[i-1][j] = count
                    i -= 1
                    count += 1
                else:
                    flag = "right"
            
        
        return res
                
                