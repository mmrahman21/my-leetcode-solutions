class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n == 0:
            return False
        
        i = 1
        
        while i < n:
            
            i <<= 1
            
            print(i)
            
        if i == n:
            return True
        else:
            return False
            
            
        