class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs = sorted(costs)
        l = len(costs)
        spent = 0
        count_ice_bars = 0
        i = 0
        
        while i < l and coins > 0:
            if coins >= costs[i]:
                count_ice_bars += 1
                coins -= costs[i]
                i += 1

            else:
                break
            
        return count_ice_bars
        