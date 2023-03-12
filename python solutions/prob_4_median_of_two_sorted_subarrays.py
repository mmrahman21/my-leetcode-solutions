'''
This is a special use of binary search
I took help from some external source, and enjoyed the learning..
'''

import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
            
        start = 0
        end = m
        
        while start <= end:
            partitionA = (start + end) // 2
            partitionB = (m + n) // 2 - partitionA
            
            
            maxLeftA = -10**7 if partitionA == 0 else nums1[partitionA - 1]
            minRightA = 10**7 if partitionA == m else nums1[partitionA]
            
            maxLeftB = -10**7 if partitionB <= 0 else nums2[partitionB - 1]
            minRightB = 10**7 if partitionB >= n else nums2[partitionB]
            
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                
                if (m+n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                
                else:
                    return min(minRightA, minRightB)
                
            elif maxLeftA > minRightB:
                end = partitionA - 1
                
            elif maxLeftB > minRightA: 
                start = partitionA + 1
                
        
        
        
        
        
        
        
        
        
        