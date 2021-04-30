class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
  
        n = len(rooms)
        visited = {key : False for key in range(n)}
        S = [0]
        visited[0] = True
        
        while S:
            v = S.pop()
            for k in rooms[v]:
                if not visited[k]:
                    S.append(k)
                    visited[k] = True
                    
        print(visited)
        for i in range(n):
            if not visited[i]:
                return False
        return True
            
   
            
            
            
            
        