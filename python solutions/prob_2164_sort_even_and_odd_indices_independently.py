class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        evens = sorted(nums[::2])
        odds = sorted(nums[1::2], reverse=True)
        
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evens[i // 2]
            
            
            else: 
                nums[i] = odds[(i - 1)//2]
        
        return nums