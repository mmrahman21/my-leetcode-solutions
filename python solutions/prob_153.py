class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l == 1:
            return nums[0]
        
        beg = 0
        end = l - 1
            
        if nums[beg] < nums[end]:
            return nums[beg]

        else:
            mid = (beg + end) // 2
            
            if beg == end:
                return nums[beg]
            elif beg == mid:
                return min(nums[mid], self.findMin(nums[mid+1:end+1]))
            elif mid == end:
                return min(nums[beg:mid], nums[mid])
            else:
                return min(self.findMin(nums[beg:mid]), nums[mid], self.findMin(nums[mid+1:end+1]))

                
            
            
        