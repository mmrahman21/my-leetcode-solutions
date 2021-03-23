class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return [[1], [1, 1]]
        
        else:
            
            result = [[1], [1, 1]]
            
            for i in range(2, numRows):
                list = []
                
                for j in range(len(result[i-1])-1):
                    list.append(result[i-1][j]+result[i-1][j+1])
                
                list.insert(0, 1)
                list.append(1)
                
                result.append(list)
                
            return result
                    
                
            
        