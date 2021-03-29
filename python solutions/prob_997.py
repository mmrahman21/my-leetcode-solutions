import numpy as np

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return N
        
        
        graph = [[0 for _ in range(N)] for _ in range(N)]
        l = len(trust)
        
        for i in range(l):
            edge = trust[i]
            graph[edge[0] - 1][edge[1] -1] += 1
            
        
        graph = np.array(graph)
            
        print(graph)
        
        for i in range(N):
            if np.sum(graph[i, :]) == 0 and np.sum(graph[:, i]) == N -1:
                return i + 1
            
        return -1
            
        
            
            
        
        