def getWords(n):
    if n == 1:
        words = ['a', 'b', 'c']    
        return words
    elif n == 2:
        words = ['ab', "ac", "ba", "bc", "ca", "cb"]
        return words
    
    sub_words = getWords(n-1)
    
    words = []
    
    for word in sub_words:
        if 'a' != word[0]:
            words.append('a'+ word)
        if 'b' != word[0]:
            words.append('b'+ word)
        if 'c' != word[0]:
            words.append('c'+word)
            
    return words
            
            
        
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        
        word_list = getWords(n)
        word_list = sorted(word_list)
        
        if k <= len(word_list):
            return word_list[k-1]
        else:
            return ""
            