class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        
        a = num % 9
        
        if a == 0:
            return 9
        else:
            return a