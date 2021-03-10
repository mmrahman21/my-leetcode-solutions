class Solution:
    
            
    def maxProduct(self, nums):
        beg = 1
        end = len(nums)-1
        
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        
        while beg <= end:
            temp_max = max(nums[beg], max_prod*nums[beg], min_prod*nums[beg])
            min_prod = min(nums[beg], min_prod*nums[beg], max_prod*nums[beg])
            beg += 1
            max_prod = temp_max
            
            if result <= max_prod:
                result = max_prod
                           
        return result
    
if __name__ =='__main__':
    print(Solution().maxProduct([2,-5,-2,-4,3]))