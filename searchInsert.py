def searchInsert(nums, target):
        beg = 0
        end = len(nums)-1
        
        mid = (beg + end) // 2
        
        while beg <= end and nums[mid]!= target:
            if target > nums[mid]:
                beg = mid + 1
                
            else: 
                end = mid - 1
            mid = (beg + end) // 2
                
            
        
        if nums[mid] == target:
            return mid
        else:
            return mid + 1
        

print(searchInsert([1,3,5,6], 0))