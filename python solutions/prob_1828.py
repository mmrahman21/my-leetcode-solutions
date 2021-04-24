class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        
        for q in queries:
            
            count = 0
            
            for p in points:
                dist_sq = (p[0] - q[0])*(p[0] - q[0]) + (p[1] - q[1])*(p[1] - q[1])
                
                if dist_sq <= q[2]*q[2]:
                    count +=1
            
            answer.append(count)
        
        return answer
                
        