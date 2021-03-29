class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dict = {item[0] : item[1] for item in knowledge} 
        l = len(s)
        
        if l == 1:
            return s
        
        i = 0
        result = ""
        while i < l:
            if s[i] != "(":
                result += s[i]
                i += 1
            else:
                j = i + 1
                key = ""
                while s[j] != ')':
                    key += s[j]
                    j += 1
                
                if key in dict.keys():
                    result += dict[key]
                else:
                    result += '?'
                i = j+1
        return result
        