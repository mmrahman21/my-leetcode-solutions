from collections import Counter
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
    
        l = len(logs)
        if l == 1:
            return [1 if i==0 else 0 for i in range(k)]
        
        user_dict = {logs[i][0]: set() for i in range(l)}
        
        for i in range(l):
            user_dict[logs[i][0]].add(logs[i][1]) 
            
        L = []
        for v in user_dict.values():
            L.append(len(v))
        print(L)
    
        
        result =[0 for _ in range(k)]
        
        for k in L:
            result[k-1] += 1
        
        return result
        
            
        