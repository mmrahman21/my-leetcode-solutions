class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        l = len(words)
        
        char_dict = {}
        for word in words:
            for ch in word:
                char_dict[ch] = char_dict.get(ch, 0) + 1
            
        for (key, val) in char_dict.items():
            if val % l != 0:
                return False
            
        return True
                
        
        