class Solution:
    def majorityElement(self, nums):
        
        i = 0
        l = len(nums)
        half = l // 2
        nums2 = sorted(nums)
        
        while i < l:
            j=i+1
            
            last_match = i
            while j < l and nums2[i] == nums2[j]:
                last_match = j
                j=j+1
            
            if (last_match - i + 1) > half:
                return nums2[i]
            
            i = j

if __name__ =='__main__':
    print(Solution().majorityElement([2 , 2, 0, 1,  1, 1, 1]))

