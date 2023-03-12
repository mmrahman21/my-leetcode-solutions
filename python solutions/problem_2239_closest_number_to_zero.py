class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        closest_num = 100001
        
        for num in nums:
            
            if abs(num) == abs(closest_num):
                closest_num = max(num, closest_num)
            elif abs(num) < abs(closest_num):
                closest_num = num
        
        return closest_num
        