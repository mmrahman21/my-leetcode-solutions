class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
    
        len_part = len(part)
        while True:
            loc = s.find(part)
            
            if loc == -1:
                return s
            else:
                s = s[:loc] + s[loc +len_part:]
               