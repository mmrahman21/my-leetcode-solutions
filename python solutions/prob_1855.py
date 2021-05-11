class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        
        distance = 0
        loc = 0
        for i in range(l1):
            for j in range(loc, l2):
                if nums2[j] >= nums1[i]:
                    distance = max(distance, j-i)
                    loc = j
                else:
                    break
        return distance
                
            
        
        