class Solution:
    def search(self, nums, target):
        beg = 0
        end = len(nums) - 1
        
        mid = (beg + end) // 2
        
        while beg < end:
            if nums[mid] == target:
                return True
            
            if nums[beg] < nums[mid]:
                if target >= nums[beg] and target < nums[mid]:
                    end = mid - 1
                else:
                    beg = mid + 1
            elif nums[mid] < nums[beg]:
                if target > nums[mid] and target <= nums[end]:
                    beg = mid + 1
                else:
                    end = mid - 1
            else:
                beg += 1
            
            mid = (beg + end) // 2
            
        
        return nums[beg] == target