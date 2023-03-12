
# 2206. Divide Array Into Equal Pairs

class Solution:
    def divideArray(self, nums) -> bool:

        n = len(nums)
        if n % 2 != 0:
            return False 

        nums = sorted(nums)

        i = 0

        while i < n:
            if nums[i] != nums[i+1]:
                return False
            i = i + 2

        return True
    
    

print(Solution().divideArray([3, 4, 2, 4, 3]))