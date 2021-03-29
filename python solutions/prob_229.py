import math 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        digits = {}
        
        result = []
        for i in range(len(nums)):
            digits[nums[i]] = digits.get(nums[i], 0) + 1
            if digits[nums[i]] > math.floor(len(nums) / 3) and nums[i] not in result:
                result.append(nums[i])
        
        # for item in dict(filter(lambda x: x[1] > math.floor(len(nums) / 3), digits.items())):
        #     result.append(item)
            
        return result
        
        