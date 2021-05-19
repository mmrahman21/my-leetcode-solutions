class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l = len(nums)
        i = 1    
        my_sum = 0
        
        while i < 2**l:
            
            j = 0
            item = []
            while j < l:
                if (1 << j) & i:
                    item.append(nums[j])
                j += 1
            
            sub_sum = 0
            for p in item:
                sub_sum ^= p
            my_sum += sub_sum 
            
            i += 1
        
        print(my_sum)
        
        return my_sum
            
        