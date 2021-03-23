class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = len(nums)
        
        if l == 0:
            return [-1, -1]
        
        beg = 0
        end = l - 1
        
        mid = 0
        
        while beg <= end:
            mid = (beg + end) // 2
            
            if nums[mid] == target:
                break
            
            if target < nums[mid]:
                end = mid - 1
            
            elif target > nums[mid]:
                beg = mid + 1
                
        
        
        if nums[mid] == target:
            left = mid
            right = mid
            
            i = left - 1
            j = right + 1
            while i >= 0 and nums[i] == target:
                left -= 1
                i -= 1
            
            while j <= end and nums[j] == target:
                right += 1
                j += 1
            
            return [left, right]
        
        else:
            return [-1, -1]
        
        