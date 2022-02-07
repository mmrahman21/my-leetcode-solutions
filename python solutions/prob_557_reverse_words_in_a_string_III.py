class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(' ')
        
        i = 0
        for t in s:
            s[i] = t[::-1]
            i += 1
        
        result = ' '.join(s)
        
        return result