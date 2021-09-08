def combination(L, k):
    if k == 0:
        return [[]]
    elif k == 1:
        return [[item] for item in L]
    
    elif len(L) == k:
        return [L]
    
    res = []
    for i in range(len(L)):
        m = L[i]
        remList = L[i+1:]
        
        for sub_result in combination(remList, k-1):
            res.append([m] + sub_result)
    
    return res
    
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        L = [i for i in range(1, n+1)]
        
        return combination(L, k)