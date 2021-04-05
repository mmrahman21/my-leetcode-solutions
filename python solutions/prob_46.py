class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        
        if l==1:
            return [nums]
        
        if l == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        
        L = []
    
        
        for i in range(l):
            new = nums[:i] +nums[i+1:]
            sublist = self.permute(new)
            for item in sublist:
                item.insert(0, nums[i])
                L.append(item)
        
        return L
        
                
        
        