class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l - 2
        
        possible = False
        
        while i >= 0:
            if nums[i] < nums[i+1]:
                possible = True
                break
            i -= 1
        
        if not possible:
            nums.sort()
        else:
        
            for j in range(i+1, l):
                if nums[j] > nums[i]:
                    index = j
            
            nums[index], nums[i] = nums[i], nums[index] # Swap to find the next greater num
            
            nums[i+1:] = nums[i+1:][::-1]   # Reverse the remaining list (i+1:) 
            
        