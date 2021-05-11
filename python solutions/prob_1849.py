class Solution:
    def splitString(self, s: str) -> bool:
        
        n = len(s)
        i = n - 1
        L = []
        
        while i > 0:
            
            if L:
               
                last = L[-1]
                num = int(s[i:last])  
            else:
                num = int(s[i:])
                
            j = i - 1
            
            num2 = 0
            
            if num == 0 and j!=0:
                if s[j] == '1':
                    L.append(i)
                    i = j
                else:
                    i -= 1
                continue
                
            elif num == 0 and j == 0:
                return s[j] == '1' 
            
            
            while num2 < num and j >=0:
                
                num2 = int(s[j:i])
                while num2 > num + 1 and num2 % 10 == 0:
                    num2 //= 10
                    i -= 1
                
                j -= 1
            
            if num2 == num + 1:
                L.append(i)
                i = j + 1 
            elif num2 == 0:
                break
                   
            else:
                   
                if L:
                    i = L[0] - 1 # Cancel previous and start from new position afresh
                    L = []
                    num = int(s[i:])
                    
                else:
                   
                    i = i - 1  # Try from new position 
                    num = int(s[i:])
        
        return len(L) > 0

                
                
            
            
        