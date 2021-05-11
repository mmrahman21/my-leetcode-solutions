
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        l = len(nums)
        
        min_distance = 1001
        
        for i in range(l):
            if nums[i] == target:
                if abs(i - start) < min_distance:
                    min_distance = abs(i - start)
                    
        return min_distance
        