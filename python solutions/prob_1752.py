class Solution:
    def check(self, nums: List[int]) -> bool:
        left = 0
        l = len(nums)
        right = l - 1
        
        i = left  + 1
        j = right - 1
        while i < l and nums[i] >= nums[left]:
            left = left + 1
            i = i + 1   
            
        while j>=0 and nums[j] <= nums[right]:
            right = right - 1
            j = j - 1
       
        
        if left == l-1 and right == 0: 
            return True
        elif left + l - right == l-1 and nums[l-1] <= nums[0]:
            return True
        else:
            return False
        
        return False
                
        