class Solution:
    def removeDuplicates(self, nums):
        
        l = len(nums)
        
        start = 0
        end = 0
        i = 1
        
        
        while i < l:
            if nums[i] == nums[i-1]:
                end = i
                i = i + 1
            else:
                j = i
                
                ind = start + 2
                
                
                while end - start > 1 and j < l:
                    nums[ind] = nums[j]
                    ind = ind + 1
                    j = j + 1
                   
                
                if (end - start - 1) > 0:
                    l = l - (end - start - 1)         
                    end = start + 2
                    start = start + 2
                    i = start + 1
                    
                else:
                    start = i
                    end = i
                    i = i + 1
                    
                
        if (end - start - 1) > 0:
            l = l - (end - start - 1) 
            
        return l
    
nums = [1, 1, 1, 1]
l = Solution().removeDuplicates(nums)

print(nums[0:l])
               
                
                        
            
