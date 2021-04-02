class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n == 1:
            return [0]
        
        if n % 2 == 0:
            result = []
            
            result = [item for item in range(1, n//2+1)]
            
            result.extend([-item for item in range(1, n//2 + 1)])
            
        else:
            result = [item for item in range(-(n-1)//2, n//2+1)]
            
        
        return result
            
            
        