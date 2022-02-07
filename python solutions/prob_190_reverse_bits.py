class Solution:
    def reverseBits(self, n: int) -> int:
        
        count = 0
        
        result = 0
        
        while count < 32:
            if n & (1 << count):
                result = result*2 + 1
            else:
                result = result * 2
                
            count +=1
        
        return result
        