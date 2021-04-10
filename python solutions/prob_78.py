class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        
        if l == 1:
            return [[], [nums[0]]]
        
        i = 1    
        result = [[]]
        
        
        while i < 2**l:
            
            j = 0
            item = []
            while j < l:
                if (1 << j) & i:
                    item.append(nums[j])
                j += 1
                
            result.append(item)
            
            i += 1
        
        print(result)
        
        return result
            
            
            
            
            
        