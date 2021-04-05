class Solution:
    def numSteps(self, s: str) -> int:
        if s=="1":
            return 0
        
        l = len(s)
        
        count = 0
        
        while l > 1:
            if s[l-1] == "0":
                new = s[0:l-1]
                s = new
                l = l-1

            else:
                new = ""
                p = l-1
                
                while p >= 0:
                    if s[p] == "0":
                        new = s[0:p] + "1" + s[p+1:]
                        s = new
                        print(s)
                        break
                    else:
                        new =s[0:p]+"0" + s[p+1:]
                        s = new
                        print(s)
                    p -= 1
               
                
            
            if s[0] == "0":
                s = "1" + s
                l = l + 1
            
            print(s)
            l = len(s)
            count += 1
                    
                    
        
        return count
            
        