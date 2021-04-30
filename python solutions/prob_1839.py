class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        l = len(word)
        
        i = 0
       
        vowel_pointer = 0
        counter = 0
        max_len = 0
        
        
        while i < l:
            if word[i] == vowels[vowel_pointer]:
                counter += 1
                if counter > max_len and vowel_pointer >= 4:
                    max_len = counter
                    
            elif counter > 0 and vowel_pointer + 1 < 5 and word[i] == vowels[vowel_pointer + 1]:
                counter += 1
                vowel_pointer += 1
                if counter > max_len and vowel_pointer >= 4:
                    max_len = counter
            else:
                
                vowel_pointer = 0
                if word[i] == vowels[vowel_pointer]:
                    counter = 1
                else:
                    counter = 0
                    
            i += 1
        
        return max_len
                
            
            
                
        