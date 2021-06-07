import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        res = 1
        
        while res < n:
            res += res<<1
        
        return res == n
        
#         log_res = math.log(n, 3)
#         print(log_res)
        
#         if math.ceil(log_res) - log_res <= 0.0000000001:
#             return True
        
#         else:
#             return False


        
        
        