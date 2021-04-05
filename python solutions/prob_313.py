class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        
        l = len(primes)
        
        L = [1]
        
        
        counts = [0 for _ in range(l)]
        
        count = 1
        
        while count < n: 
            
            next_ugly = min([L[counts[i]]*primes[i] for i in range(l)])
            L.append(next_ugly)
            
            for i in range(l):
                if next_ugly % primes[i] == 0:
                    counts[i] += 1
        

            count += 1
        
        return L[-1]