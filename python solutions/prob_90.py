class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        
        if l == 1:
            return [[], [nums[0]]]
        
        nums = sorted(nums)
        i = 1    
        result = [[]]
        
        
        while i < 2**l:
            
            j = 0
            item = []
            while j < l:
                if (1 << j) & i:
                    item.append(nums[j])
                j += 1
                
            if item not in result:
                result.append(item)
            
            i += 1
        
        print(result)
        
        return result
            
            
            
            
            
        
        