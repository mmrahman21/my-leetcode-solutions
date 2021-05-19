class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        
        total = sum(nums)
        
        l = len(nums)
        
        i = l - 1
        
        while i >= 0:
            curr_sum = sum(nums[i:])
            if curr_sum > total - curr_sum:
                return nums[i:][::-1]
            i -= 1
            
            
        