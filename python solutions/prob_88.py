class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n != 0:
            if m == 0:
                nums1[0:n] = nums2
            else:
                p = m - 1
                q = n - 1
                
                while p >= 0 and q >= 0:
                    if nums1[p] >= nums2[q]:
                        nums1[p+q+1] = nums1[p]
                        p -= 1
                    else:
                        nums1[p+q+1] = nums2[q]
                        q -= 1
                
                while q >=0:
                    nums1[q] = nums2[q]
                    q -= 1         
                
        else:
            pass
        
        
nums1 = [1,2,3,0,0,0]

Solution().merge(nums1, 3, [2,5,6], 3)
print(nums1)