class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l==1:
            return nums[0]
        
        beg = 0
        end = l - 1
        
        minimum = 5001
        
        while beg <= end:
             
            while beg >=0 and end >=0 and nums[beg] == nums[end]:
                if minimum > nums[beg]:
                    minimum = nums[beg]
                beg += 1
                end -= 1
                  
            if beg > end:
                break 
                
            elif nums[beg] < nums[end]:
                return min(minimum, nums[beg])
            
            else:
                mid = (beg + end) // 2
                if beg == end:
                    return min(minimum, nums[beg])
                
                elif beg == mid:
                    return min(minimum, nums[mid], self.findMin(nums[mid+1:end+1]))
                elif mid == end:
                    return min(minimum, nums[mid], self.findMin(nums[beg:mid]))
                else:
                    return min(minimum, nums[mid], self.findMin(nums[beg:mid]), self.findMin(nums[mid+1:end+1]))
        
        return minimum
        