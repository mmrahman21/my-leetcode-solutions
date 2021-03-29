sol = {}

def maxLength(s, i, j):
    if (i, j) in sol.keys():
        return sol[(i,j)]
    
    elif j - i + 1 == 1:
        sol[(i, j)] = -1 
        return sol[(i, j)]

    elif j - i + 1 == 2:

        if s[i] == s[j]:
            sol[(i, j)] = 0
            
        else:
            sol[(i, j)] = -1
            
        return sol[(i,j)]
    
    elif s[i] == s[j]:
        sol[(i,j)] = j - i + 1 - 2
        return sol[(i,j)]
    
    else:
        result1 = maxLength(s, i+1, j)
        result2 = maxLength(s, i, j-1)

        sol[(i, j)] = result1 if result1 > result2 else result2

        return sol[(i,j)]
    
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        l = len(s)
        result = maxLength(s, 0, l-1)
        sol.clear()
        return result
        
        
        
        