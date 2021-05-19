from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.map1 = Counter(nums1)
        self.map2 = Counter(self.nums2)
        
    def add(self, index: int, val: int) -> None:
        self.map2[self.nums2[index]] = max(0, self.map2[self.nums2[index]] - 1)
        self.nums2[index] += val
        self.map2[self.nums2[index]] = self.map2.get(self.nums2[index], 0) + 1

    def count(self, tot: int) -> int:
        pair_count = 0
        for (key, val) in self.map1.items():
            pair_count += val*self.map2[tot - key]
        
        return pair_count
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)