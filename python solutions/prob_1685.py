class Solution:
    def getSumAbsoluteDifferences(self, nums):
        l = len(nums)
        
        result = []
        
        result.append(sum([nums[i] - nums[0] for i in range(l)]))
        
        for j in range(1, l):
            item = result[j-1]+(j-1)*(nums[j] - nums[j-1]) - (l - j - 1)*(nums[j] - nums[j-1])
            result.append(item)
            
        return result