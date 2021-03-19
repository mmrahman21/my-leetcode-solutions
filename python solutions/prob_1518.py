class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        if numBottles < numExchange:
            return numBottles
        
        else:
            rem = numBottles % numExchange
            quotient = numBottles // numExchange
            return (numBottles - rem)  + self.numWaterBottles(quotient+rem, numExchange)
            
            
print(Solution().numWaterBottles(15, 4))