class Solution:
    def twoEggDrop(self, n: int) -> int:
        count = 1
        decrement = 0
        
        while n > count: 
            decrement += 1
            count += 1
            n -= decrement
        
        return count
            
        