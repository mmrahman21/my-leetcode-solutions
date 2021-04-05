class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        w = self.countAndSay(n-1)
        print(w)
        
        l = len(w)
        i=0
        count = 1
        result = ""
        while i < l:
            if i == l-1:
                result +=str(count) + str(w[i]) 
                break
                
            elif w[i] == w[i+1]:
                count +=1
            
            else:
                result +=str(count) + str(w[i])
                count = 1
            i += 1
        
            
        return result
            
                
            
            
        