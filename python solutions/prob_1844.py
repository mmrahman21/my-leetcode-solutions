class Solution:
    def replaceDigits(self, s: str) -> str:
        
        l = len(s)
        result = s[0]
        for i in range(1, l):
            if i % 2 == 1:
                result += chr(ord(s[i-1]) + int(s[i]))
            else:
                result += s[i]

        return result
            
        