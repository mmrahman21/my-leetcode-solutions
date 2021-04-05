class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        large_gap = 0
        loc = -1
        sum_diff = 0
        l= len(nums1)
        L = []
        for i in range(l):
            n = abs(nums1[i]-nums2[i]) 
            if n > large_gap:
                large_gap = abs(nums1[i]-nums2[i])
                loc = i 
            sum_diff += n
            sum_diff = sum_diff % (10**9 + 7)
            
            
        if sum_diff == 0:
            return sum_diff
        
        else:
            for i in range(l):
                t = abs(nums1[i] - nums2[loc])
                L.append(t)
                
            print(sum_diff)
            print(loc)
        
            sum_diff -= abs(nums1[loc] - nums2[loc])
            sum_diff += min(L)
        
            return sum_diff % (10**9 + 7)
            
                
        