class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        L = [1]
        
        last = 1
        
        twoCount = 0
        threeCount = 0
        fiveCount = 0
        
        count = 1
        
        while count < n: 
            next_ugly = min(L[twoCount]*2, L[threeCount]*3, L[fiveCount]*5)
            L.append(next_ugly)
        
            if next_ugly % 2 == 0:
                twoCount += 1

            if next_ugly % 3 == 0:
                threeCount += 1
                
            if next_ugly % 5 == 0:
                fiveCount += 1
            count += 1
        
            
        return L[-1]
        
        
        
            
            
        