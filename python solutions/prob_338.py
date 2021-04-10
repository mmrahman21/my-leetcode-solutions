class Solution:
    def countBits(self, num: int) -> List[int]:
        
        if num == 0:
            return [0]
        
        result = [0]
        i = 1
        
        while i <= num:
        
            if i % 2 == 1:
                result.append(result[i-1]+1)
            else:    
                result.append(result[i//2])

            i += 1

            
        return result
                
                
                
                
                
                
        