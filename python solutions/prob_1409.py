class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        P = [i for i in range(1, m+1)]
        
        i = 0
        l = len(queries)
        res = []
        
        while i < l:
            j = 0
            
            while j < m:
                if queries[i] == P[j]:
                    P.remove(P[j])
                    P.insert(0, queries[i])
                    res.append(j)
                    break
                j += 1
            
            i += 1
        
        return res
                
        
        
        