class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l = len(nums)
        
        i = 0
        out = -1
        
        while i < l - 1:
            j = i+ 1
            
            while j < l:
                if nums[j] > nums[i] and nums[j] - nums[i] > out:
                    out = nums[j] - nums[i]
                    print(nums[j], nums[i])
                j += 1
            i += 1
        
        return out
    
    # Another person's solution:
    # def maximumDifference(self, nums: List[int]) -> int:
    #     ans = 0
    #     prefix = inf
    #     for i, x in enumerate(nums): 
    #         if i: ans = max(ans, x - prefix)
    #         prefix = min(prefix, x)
    #     return ans if ans > 0 else -1
        