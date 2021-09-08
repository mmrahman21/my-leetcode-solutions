import math
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        
        prime_list = [True]*n
        prime_list[0] = prime_list[1] = False
        
        i = 2
        while i <= int(math.sqrt(n)):
            if prime_list[i]:
                for j in range(i*i, n, i):
                    prime_list[j] = False
                    
            i += 1
        
        return sum(prime_list)
        