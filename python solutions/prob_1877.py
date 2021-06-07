class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        
        l = len(nums)
        
        max_sum = 0
        
        while i < l/2:
            if nums[i] + nums[l-1-i] > max_sum:
                max_sum = nums[i] + nums[l-1-i]
            i += 1
        
        return max_sum
        