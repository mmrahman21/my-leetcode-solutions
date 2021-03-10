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
    
    
if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    