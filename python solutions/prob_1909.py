class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            p = nums[:i]
            p.extend(nums[i+1:])
            res = all(i < j for i, j in zip(p, p[1:]))
            if res:
                return True

        
        return False
            
                
        