class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        left = 0
        
        right = n-1
        
        while left <= right:
            while True:
                if left > right:
                    break
                elif nums[left]**2 < nums[right]**2:
                    nums[right] = nums[right]**2
                    right -= 1
                else:
                    break
            
            
            nums.insert(right + 1, nums[left]**2)
            nums.pop(0)
            right -= 1
            
        
        print(nums)
        
        return nums
        