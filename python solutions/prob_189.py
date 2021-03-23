class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        
        k = k % l
        
        if k >= l // 2:
            for i in range(l-k):
                item = nums.pop(0)
                nums.append(item)
        else:
            i = 0
            while i < k:
                item = nums.pop()
                nums.insert(0, item)
                i += 1

num = [1, 2, 3, 4, 5, 6]
Solution().rotate(num, 4)
print(num)
            
        