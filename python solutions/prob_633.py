class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        if c == 0 or c == 1:
            return True
        
        i = 1
        
        while i*i <= c: 
            if int(sqrt(c - i*i))*int(sqrt(c - i*i)) == c - i*i:
                return True
            
            i += 1
            
        return False
            
        