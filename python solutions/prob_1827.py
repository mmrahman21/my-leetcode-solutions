class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops_count = 0
        
        l = len(nums)
        
        i = 1
        
        while i < l:
            if nums[i] <= nums[i-1]:
                ops_count += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
            i += 1
        
        return ops_count
        