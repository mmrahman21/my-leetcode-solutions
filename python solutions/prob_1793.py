class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = len(nums)
        
        if l == 1:
            return nums[0]
        
        i = k 
        j = k 
       
        glob_min = nums[k]
        score = nums[k]
        
        while i >=0 and j < l:
            glob_min = min(nums[i], nums[j], glob_min)
            score =max(score, glob_min*(j-i+1))
            
            if i == 0:
                j += 1
                continue
            if j == l-1:
                i -= 1
                continue
            
            if nums[i-1] > nums[j+1]:
                i -= 1
            else:
                j += 1
            
        return score
            
        
                
            
            
        