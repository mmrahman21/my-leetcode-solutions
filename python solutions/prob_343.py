class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        elif n == 5:
            return 6
        elif n == 6:
            return 9
        
        result = [1, 2, 4, 6, 9]
        
        
        i = 7
        
        while i <= n:
            item = result[-3]*3
            result.append(item)
            i += 1
        
    
        return result[-1]
        