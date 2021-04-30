class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        
        l1 = len(arr1)
        l2 = len(arr2)
        ans1 = 0
        ans2 = 0
        
        for i in range(l1):
            ans1 ^=arr1[i]
            
        for j in range(l2):
            ans2 ^=arr2[j]
            
        return ans1 & ans2
        