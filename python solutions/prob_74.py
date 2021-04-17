class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        start = 0
        end = m*n - 1
        
        mid = (start + end) // 2
        
        i, j = mid // n, mid % n
        
        while start <= end:
            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                end = mid - 1
            else:
                start = mid + 1
            
            mid = (start + end) // 2
            i, j = mid // n, mid % n
        
        return False
                
                
                
        