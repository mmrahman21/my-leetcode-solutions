class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        l = len(nums)
        
        items_dict = {}
                
        result = []
       
        for item in nums:
            items_dict[item] = items_dict.get(item, 0) + 1
            
            
        keys = sorted(items_dict.values())[-k:]
        
        for kk in items_dict.keys():
            if items_dict[kk] in keys:
                result.append(kk)
        
        return result
        