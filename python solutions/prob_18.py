class Solution:
    def threeSum(self, nums, target):
        
        list = []
        
        for i in range(0, len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > target and target >=0:
                return list
            
            left = i+1
            right = len(nums) - 1
            
            while left < right:
                
                n = nums[i]+nums[left]+nums[right]
                
                if  n == target:
                    list.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
                elif n > target:
                    right -= 1
                else:
                    left += 1
                      
        return list
    
    def fourSum(self, nums, target):
        if len(nums) <=3:
            return []
        nums = sorted(nums)
        list = []
        for i in range(0, len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > target and target >=0:
                return list
            three_list = self.threeSum(nums[i+1:], target-nums[i])
            
            if three_list != []:
                for l in three_list:
                    list.append([nums[i]] + l)
        
        return list
                
print(Solution().fourSum([1,-2,-5,-4,-3,3,3,5], -11))