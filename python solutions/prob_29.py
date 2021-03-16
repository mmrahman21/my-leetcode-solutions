
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == 0:
            return 0
        
        if dividend * divisor >= 0:
            sign = 1
        else:
            sign = -1
            
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if divisor == 1:
            quotient = dividend
        else:
            quotient = 0
            
            i = 31
            temp = 0
            while i >= 0:
                if temp + (divisor << i) <= dividend:
                    temp = temp + (divisor << i)
                    quotient = quotient | (1 << i)
                i -= 1
            
        if sign*quotient > (1 << 31) - 1:
            return sign*((1 << 31) - 1)
        elif sign*quotient < -(1 << 31):
            return -(1 << 31)
        else:
            return sign*quotient
        