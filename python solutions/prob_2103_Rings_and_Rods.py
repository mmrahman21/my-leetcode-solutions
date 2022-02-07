class Solution:
    def countPoints(self, rings: str) -> int:
        my_dict = {k:set() for k in range(10)}
        
        l = len(rings)
        count = 0
        
        ch = 0
        while ch < l:
            my_dict[int(rings[ch+1])].add(rings[ch]) 
            ch += 2
            
        for k in my_dict.keys():
            if len(my_dict[k]) == 3:
                count += 1
                
        
        return count
            