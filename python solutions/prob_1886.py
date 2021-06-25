def check_mat_equal(n, mat1, mat2):
    for i in range(n):
        for j in range(n):
            if mat1[i][j] != mat2[i][j]:
                return False
    return True
    
    
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n = len(mat)
        
        count = 0
        flag = check_mat_equal(n, mat, target)
    
        while not flag:
            
            for i in range(n // 2):
                for j in range(i, n - i - 1):
                    temp = mat[i][j]
                    mat[i][j] = mat[n-1-j][i]
                    mat[n-1-j][i] = mat[n - 1 -i][n - 1 - j]
                    mat[n - 1 -i][n - 1 - j] = mat[j][n - 1 - i]
                    mat[j][n - 1 - i] = temp
            count += 1
            flag = check_mat_equal(n, mat, target)
            
            if count >= 4:
                break
                
        return flag
            
                    
            
        