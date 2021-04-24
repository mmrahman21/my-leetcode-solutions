class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        answer = []
        
        xor = 0
        
        for num in nums:
            xor ^= num 
        
        l = len(nums)
        
        limit = (1 << maximumBit) - 1
        
        while l > 0:   
            
            k = limit ^ xor
            answer.append(k)
            
            xor ^= nums[l-1]
            
            l -= 1
        
        return answer
        
        
            
        