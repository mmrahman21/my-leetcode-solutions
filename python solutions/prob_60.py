class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        
        l = len(nums)
        
        p = 1
        while p < k:

            i = l - 2

            possible = False

            while i >= 0:
                if nums[i] < nums[i+1]:
                    possible = True
                    break
                i -= 1

            if not possible:
                nums.sort()
            else:

                for j in range(i+1, l):
                    if nums[j] > nums[i]:
                        index = j

                nums[index], nums[i] = nums[i], nums[index] # Swap to find the next greater num
                
                # Reverse the remaining list (i+1:)
                # This is required because swapping already guaranteed larger number
                # Reversing of the remaining required to ensure that it is the next greater

                nums[i+1:] = nums[i+1:][::-1]   
            
            p += 1
        
        res = ''.join([str(ele) for ele in nums])
        
        return res