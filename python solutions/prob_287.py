class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = sum(nums)
        
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i], 0) + 1
            
            if dict[nums[i]] == 2:
                return nums[i]
        
        
        