class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        
        L =[1]
        
        twoCount = 0
        threeCount = 0
        fiveCount = 0
        
        last = 1
        
        while last < n:
            last = min(L[twoCount]*2, L[threeCount]*3, L[fiveCount]*5)
            L.append(last)
            
            if last % 2 == 0:
                twoCount += 1
            if last % 3 == 0:
                threeCount += 1
            if last % 5 == 0:
                fiveCount += 1
        
        if last == n:
            return True
        else:
            return False
        
        