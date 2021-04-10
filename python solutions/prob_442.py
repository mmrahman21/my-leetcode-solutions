class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        
        n = len(nums)
        
        res = []
        
        for j in range(n):
            
            nums[nums[j] % (n+1) - 1] = nums[nums[j]  % (n+1) - 1] + n+1
            
        print(nums)
            
        for j in range(n):
            
            if nums[j] // (n+1) >= 2:
                res.append(j+1)
                
                
        return res
            
        
                
            
        
            
        
       
        
        
        