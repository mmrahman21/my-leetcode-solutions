# It can be solved using O(n) algorithm
# No need to use divide and conquer technique as used here. 

class Solution:
    
    def maxCrossSubArray(self, nums, low, mid, high):
        left_sum = - 100001
        i = mid
        sum = 0
        while i >= low:
            sum = sum + nums[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i
            i -= 1
        right_sum = - 100001
        sum = 0
        j = mid + 1
        while j <= high:
            sum = sum + nums[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j
            j += 1
            
        return (i, j, left_sum+right_sum)
    
    def maxSubArrayHandler(self, nums, low, high):
        
        if low == high: 
            return (low, high, nums[low])
        else:
            mid = (low + high) // 2
            (left_low, left_high, left_result) = self.maxSubArrayHandler(nums, low, mid)
            (right_low, right_high, right_result) = self.maxSubArrayHandler(nums, mid+1, high)
            (cross_low, cross_high, cross_result) = self.maxCrossSubArray(nums, low, mid, high)
        
        if left_result >= right_result and left_result >= cross_result:
            return (left_low, left_high, left_result)
        elif right_result >= left_result and right_result >= cross_result:
            return (right_low, right_high, right_result)
        else:
            return (cross_low, cross_high, cross_result)
        
            
    def maxSubArray(self, nums):
        beg = 0
        end = len(nums)-1
        (i, j, result) = self.maxSubArrayHandler(nums, beg, end)
        return result
    
    def maxProfit(self, prices):
        
        if len(prices) <= 1:
            return 0
        
        price_changes =[]
        for i in range(len(prices)-1):
            price_changes.append(prices[i+1] - prices[i])
            
        print(price_changes)
        
        result = self.maxSubArray(price_changes)
        
        if result < 0:
            return 0
        else:
            return result
    

print(Solution().maxProfit([1]))

        