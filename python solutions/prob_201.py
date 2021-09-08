class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        result = 0
        
        while left > 0 and right > 0:
            i = 1
            msb_left = -1

            while i <= left:
                i <<= 1
                msb_left += 1
                
            i = 1
            msb_right = -1
            
            while i <= right:
                i <<= 1
                msb_right += 1
            
            if msb_left == msb_right:
                result +=2**msb_right
                left -= 2**msb_right
                right -= 2**msb_right
            else:
                break
            
        return result
                
            
            
            
        