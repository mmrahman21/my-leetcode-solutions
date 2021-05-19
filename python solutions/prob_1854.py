class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        res = [0 for _ in range(1950, 2051)]
        
        for item in logs:
            
            res[item[0] - 1950:item[1] - 1950] = [res[p - 1950] + 1 for p in range(item[0], item[1])]
        
        max_val = max(res)
        
        return 1950 + res.index(max_val)
        