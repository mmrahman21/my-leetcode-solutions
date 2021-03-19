class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        count_five_as_factors = 0
        div = 5
        
        while True:
            
            if div > n:
                break
                
            count_five_as_factors += (n // div)
            div *= 5
            
        count_two_as_factors = 0
        div = 2
        
        while True:
            if div > n:
                break
            count_two_as_factors += (n // div)
            div *= 2
        
        return min(count_five_as_factors, count_two_as_factors)
    
print(Solution().trailingZeroes(1000))
        