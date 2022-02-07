class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        l = len(s1)
        
        if len(s1) > len(s2):
            return False
        
        dic1 = {}
        for k1 in s1:
            dic1[k1] = dic1.get(k1, 0) + 1
        
        for start in range(len(s2) - l+1):
            substr = s2[start:start+l]
            
            dic2 = {}
            for k2 in substr:
                dic2[k2] = dic2.get(k2, 0) + 1
                
            if dic1 == dic2:
                return True
        
        return False
    

sol = Solution()

print(sol.checkInclusion("ab", "diebbbasss"))
        
            
            
        
            
            
        