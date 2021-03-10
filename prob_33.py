class Solution:
    def search(self, nums, target: int) -> int:
        l = len(nums)
        beg = 0
        end = l - 1
        
        mid = (beg + end) // 2
        
        while beg <= end and nums[mid]!=target:
            
        
            if nums[beg] <= nums[mid]:
                
                if target > nums[mid] or target < nums[beg]:
                    beg = mid + 1
                    
                else:
                    end = mid - 1
            
            else:
                
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    beg = mid + 1
            
            
            mid = (beg + end) // 2
            
        if nums[mid] == target:
            return mid
        else:
            return -1
        
print(Solution().search([4,5,6,7,0,1,2], 3))
            
            
            
                
                
            