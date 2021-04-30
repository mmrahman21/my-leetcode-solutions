class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        L = matrix[0]
        
        if n > 1:
            i = 1
        else:
            i = 0
            
        j = 0
        
        start = 0
        end = len(L) - 1
        
        while end < n*n - 1:
           
            item = matrix[i][j]
            
            mid = (start + end) // 2
            
            loc = 0
            
            while start <= end:
                print(start, end)
                
                if start == end:
                    if L[start] < item:
                        loc = start + 1
                    else:
                        loc = start
                    break
                 
                elif L[mid] == item:
                    loc = mid + 1
                    break
                elif L[mid] > item:
                    end = mid - 1
                else:
                    start = mid + 1

                    
                mid = (start + end) // 2
            
            if loc == 0:
                loc = end + 1
            
            
            L.insert(loc, item)
            start = 0
            end = len(L) - 1
            
            if j == n-1:
                i += 1
                j = 0
            else:
                j += 1
            
            
        return L[k-1]
        
        
        