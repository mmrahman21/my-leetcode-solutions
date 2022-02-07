class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        l = len(nums)
        
        i = 0
        res = 0
        
        while i < l-1:
            j = i + 1
            while j < l:
                if abs(nums[i] - nums[j]) == k:
                    res += 1
                j += 1
            i += 1
        
        return res
            
            
        