class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        l = len(words)
        
        i = 0
        result = []
        while i < l:
            j = 0
            
            while j < l:
                if j== i:
                    j += 1
                    continue
                    
                elif len(words[i]) > len(words[j]):
                    pass
                else:
                    if words[i] in words[j] and words[i] not in result:
                        result.append(words[i])
                j += 1
            
            i += 1
            
        return result
                    
                    
            
        