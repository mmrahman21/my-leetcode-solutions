class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        
        if len(sentence1) == 0 or len(sentence2) == 0:
            return True

        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        
        if sentence1[0] == sentence2[0]: 
            
            sentence1 = ' '.join(sentence1[1:])
            sentence2 = ' '.join(sentence2[1:])
            return self.areSentencesSimilar(sentence1, sentence2)
        
        elif sentence1[len(sentence1) - 1] == sentence2[len(sentence2)-1]:
            sentence1 = ' '.join(sentence1[:-1])
            sentence2 = ' '.join(sentence2[:-1])
            return self.areSentencesSimilar(sentence1, sentence2)
        
        else:
            return False
        
       
        