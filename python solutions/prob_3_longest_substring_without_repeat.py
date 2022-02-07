class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = len(s)
        
        if l == 0:
            return 0
        
        result = s[0]
        result_len = 1
        
        i = 0
        j = i+1
        
        while i < j and j < l:
           
            substr = s[i:j+1]
            if len(set(substr)) == j-i + 1:
                
                if j-i+1 >= result_len:
                    result_len = j - i + 1
                    result = substr
                j = j + 1
                
            else:
                loc = substr.find(substr[-1])
                i = i+loc+1
                j = j + 1

                    
        return result_len
                
            
        