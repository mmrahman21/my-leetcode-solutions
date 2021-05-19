class Solution:
    def sortSentence(self, s: str) -> str:
        word_dict = {}
        
        s = list(s.split(" "))
        
        word_count = len(s)
        
        res = ""
        
        for word in s:
            i = 0
            while word[i] > '9':
                i += 1
            
            word_dict[word[i:]] = word[:i]
        
        for i in range(1, word_count+1):
            res +=word_dict[str(i)]
            if i != word_count:
                res += " "
        
        return res
            
        
        