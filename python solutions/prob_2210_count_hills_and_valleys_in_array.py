class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        res = []
        res.append(nums[0])
        
        for item in nums[1:]:
            if item != res[-1]:
                res.append(item)
                
        nums = res
        
        l = len(nums)
        
        count_hills_valleys = 0
        
        i = 1
        
        while i < l-1:
                
            if (nums[i]- nums[i-1])*(nums[i] - nums[i+1]) > 0:
                count_hills_valleys += 1
                
            i += 1
        
        return count_hills_valleys
                
        
            
            
            
            
            
            
            
        
        
        