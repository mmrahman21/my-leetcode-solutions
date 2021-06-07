class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        i = 0
        l = len(s)
        count = 0
        
        while i <= l- 3:
            x = s[i:i+3]
            if len(set(x)) == 3:
                count += 1
            i += 1
        
        return count
        