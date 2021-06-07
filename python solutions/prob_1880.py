class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        l1 = len(firstWord)
        l2 = len(secondWord)
        l3 = len(targetWord)
        
        l = max(l1, l2, l3)
        
        a, b, c = 0, 0, 0
        i = 0
        
        while True:
            
            if i < l1:
                a = 10*a + ord(firstWord[i]) - ord('a')
            if i < l2:
                b = 10*b + ord(secondWord[i]) - ord('a')
            if i < l3:
                c = 10*c + ord(targetWord[i]) - ord('a')
            
            i += 1
            if i >= l:
                break
        return a + b == c
            