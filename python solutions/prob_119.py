class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        elif rowIndex == 1:
            return [1, 1]
        
        else:
            
            result = [1, 1]
            
            for i in range(2, rowIndex+1):
                list = []
                
                for j in range(len(result) - 1):
                    list.append(result[j] + result[j+1])
                
                list.insert(0, 1)
                list.append(1)
                
                result = list
            
            return result
            
        