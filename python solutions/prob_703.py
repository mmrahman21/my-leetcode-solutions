from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapify(self.heap)
        
        for num in nums:
            if len(self.heap) < self.k:
                heappush(self.heap, num)
            else:
                if num > self.heap[0]:
                    heappushpop(self.heap, num)
        

    def add(self, val: int) -> int:
        
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heappushpop(self.heap, val)
            
                      
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)