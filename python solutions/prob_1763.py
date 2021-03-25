class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        l = len(s)
        
        nice_length = 0
        ans_string = ""
        for i in range(l-1):
            for j in range(i+1, l):
                p = s[i:j+1]
               
                q = p.lower()
                
                if p == q:
                    continue
                
                flag = True
                for char in p:
                    if char.isupper():
                        if char.lower() not in p:
                            flag = False
                            break
                    if char.islower():
                        if char.upper() not in p:
                            flag = False
                            break
                            
                if flag == True:
                    if nice_length < max(nice_length, len(p)):
                        nice_length = len(p)
                        ans_string = p
                        print(ans_string)
                        
        return ans_string
                        
                    
                    
            
                
                
        