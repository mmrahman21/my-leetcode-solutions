class Solution:
    def productExceptSelf(self, nums):
        
        ans = []
        l = len(nums)
        
        forward_product = 1
        i = 0
        while i < l:
            ans.append(forward_product)
            forward_product  *= nums[i]
            i = i + 1
        
        reverse_prod = 1
        
        j = l - 1
        while j >= 0:
            ans[j] = reverse_prod * ans[j]
            reverse_prod *= nums[j]
            j = j - 1
            
        return ans
    
if __name__== "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
    
            
        