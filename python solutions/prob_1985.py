from collections import defaultdict

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        sorted_array = []
        data = defaultdict(list)
        
        for item in nums:
            data[len(item)].append(item)
        
        
        for p in sorted(data.keys()):
            sorted_array.extend(sorted(data[p]))
        
        return sorted_array[-k]