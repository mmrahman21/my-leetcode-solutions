def missNumber(nums):
    ans = 0
    
    for i in range(len(nums)):
        ans ^=nums[i]
    print(ans)
    for i in range(len(nums)+1):
        ans ^=i
        print(ans)
    return ans

class Solution:
    def missingNumber(self, nums) -> int:
        
        n = len(nums)
        
        my_sum = (n*(n+1))// 2
        
        return my_sum - sum(nums) 
    
        
print(missNumber([1, 4, 0, 3]))