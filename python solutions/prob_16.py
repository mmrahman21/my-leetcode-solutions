class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        
        l = len(nums)
        i = 0
       
        result = target
        diff = float('Inf')
        for i in range(len(nums) - 2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left = i + 1
            right = l - 1
            
            while left < right:
                num = nums[i] + nums[right] + nums[left]
                
                if num == target:
                    return num
                
                if abs(num - target) < diff:
                    result = num
                    diff = abs(num - target)
                    
                if num > target:
                    right -= 1
                if num < target:
                    left += 1
                
        return result
        
        