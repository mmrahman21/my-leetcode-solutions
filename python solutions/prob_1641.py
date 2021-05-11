def countVowel(n, start):
    if n == 1:
        return 5 - start
    elif start == 4:
        return 1
    else:
        res = 0
        for i in range(start, 5):
            res += countVowel(n-1, i)
        return res
    
class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        return countVowel(n, 0)
        