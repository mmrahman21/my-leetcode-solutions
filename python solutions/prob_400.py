class Solution:
    def findNthDigit(self, n: int) -> int:
        
        if n <= 9:
            return n
        
        my_sum = 9
        
        factor = 9
        i = 2
        
        while my_sum < n:
            my_sum = my_sum + i*factor*10
            factor *= 10
            i += 1
            
        i = i-1
       
        my_sum -= factor*i
        
        p = factor // 9
        
        offset = (n - my_sum) // i
        digit = (n - my_sum) % i
        
        q = (p - 1) + offset
       
        if digit == 0:
            return q % 10
        else:
            q = q + 1
            counter = 0
            while counter <= i - 1 - digit:
                q = q // 10
                counter += 1
            return q % 10
        