from collections import Counter
class Solution:
    def singleNumber(self, nums):
        dict = Counter(nums)
        
        for key in dict.keys():
            if dict[key] == 1:
                return key

print(Solution().singleNumber([2, 2, 3, 4, 4]))