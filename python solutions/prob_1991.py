class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        middle_index = 0
        l = len(nums)
        
        while left != right and middle_index < l:
            if middle_index == l - 1:
                break
            left += nums[middle_index] 
            middle_index += 1
            right -= nums[middle_index]
            
        if left == right:
            return middle_index
        else:
            return -1 
        
        
        