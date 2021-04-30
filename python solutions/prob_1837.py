class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        my_sum = 0
        
        while n!= 0:
            my_sum += n % k
            n = n // k
        
        return my_sum
            
            
        