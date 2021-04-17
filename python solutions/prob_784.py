class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        if S.isdigit():
            return [S]
        
        i = 0
        l = len(S)
        result = []
        while i < l:
            if S[i].isalpha():
                if i < l -1:
                    
                    sub_result = self.letterCasePermutation(S[i+1:])
                    my_string1 = S[:i+1]
                    my_string2 = S[:i] + chr(ord(S[i]) ^ (1 << 5))  # change case
                    for item in sub_result:
                        result.append(my_string1+item)
                        result.append(my_string2+item)
                else:
                    my_string1 = S[:i+1]
                    my_string2 = S[:i] + chr(ord(S[i]) ^ (1 << 5))  # change case
                    result.append(my_string1)
                    result.append(my_string2)
                    
                break
              
                
            i += 1
            
        return result
        
        
       
            
        