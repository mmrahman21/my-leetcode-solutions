class Solution:
    def removeDuplicates(self, nums):
        l = len(nums)
        
        last_updated = 0
        
        i = 0
        
        while i < l:
            
            j = i + 1
            
            
            while j < l and nums[i] == nums[j]:
                j = j+1
                
            nums[last_updated] = nums[j-1] 
            i = j
            last_updated += 1
            
        
        return last_updated

nums = [0,0,1,1,1,2,2,3,3,4]
    
print(nums)
print(Solution().removeDuplicates(nums))
print(nums)
            
            
            