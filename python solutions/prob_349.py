class Solution:
    def intersection(self, nums1, nums2):
        
        p = len(nums1)
        q = len(nums2)
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        result = []
        
        i , j = 0, 0
        
        while i < p and j < q:
             
            m = i + 1
            while m < p and nums1[m] == nums1[i]:
                m = m + 1
            i = m - 1

            n = j + 1
            while n < q and nums2[n] == nums2[j]:
                n = n + 1
            j = n - 1
            
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i = i + 1
                j = j + 1
            
            elif nums1[i] < nums2[j]:
                i = i + 1
            else:
                j = j + 1
        
        return result
          
          
          
print(Solution().intersection([1, 4, 4, 1], [4, 1]))