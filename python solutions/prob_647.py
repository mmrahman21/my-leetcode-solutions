
def palindrome(s):
    if s == s[-1::-1]:
        return True
    
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        
        if l == 1:
            return 1
        
        count = 0
        
        dp ={}
        
        i = 0
        while i < l-1:
            j = l - 1
            
            while j > i:
                if (i, j) in dp.keys():
                    count += 1
                    j -= 1

                elif palindrome(s[i:j+1]):
                    count += 1
                    p = i
                    q = j
                    while p < q:
                        dp[(p, q)] = 1
                        p += 1
                        q -= 1
                    j -= 1
                else:
                    j -= 1
            i += 1
            
        count += l
            
        return count
            
                
                
                
        
        
        
        