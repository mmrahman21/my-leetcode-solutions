class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        l = len(word)
        if l == 1:
            if word.isdigit():
                return 1
        
        i = 0
        result = []
        while i < l:
            res_string = ""
            
            if word[i].isdigit(): 
                j = i
                while j < l and word[j].isdigit():
                    res_string +=word[j]
                    j += 1
                if len(res_string) > 0 and int(res_string) not in result:
                    result.append(int(res_string))
                i = j
            else:
                i += 1
        
        return len(result)
            
                
        