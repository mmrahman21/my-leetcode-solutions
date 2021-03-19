class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1 or num == 4 or num == 9:
            return True
        
        last_digit = num % 10
        
        if last_digit == 2 or last_digit == 3 or last_digit == 7 or last_digit == 8:
            return False
        
        half = num // 2 + 1

        for i in range(2, half, 1):
             
            if i*i > num:
                return False
            if num % (i*i) == 0:
                return self.isPerfectSquare(num // (i*i))
        
        return False
            
        