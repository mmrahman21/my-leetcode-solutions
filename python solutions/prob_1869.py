class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        one_count = 0
        zero_count = 0
        
        one_max = 0
        zero_max = 0
        
        l = len(s)
        
        i = 0
        
        while i < l:
            
            if s[i] == '1':
                
                one_count = 0
                while i < l and s[i] == '1':
                    one_count += 1
                    i += 1
                
                if one_count > one_max:
                    one_max = one_count
            if i == l:
                break
                
            if s[i] == '0':
                zero_count = 0
                while i < l and s[i] == '0':
                    zero_count += 1
                    i += 1
                if zero_count > zero_max:
                    zero_max = zero_count
            
        return one_max > zero_max
            
                
                
                
        
        