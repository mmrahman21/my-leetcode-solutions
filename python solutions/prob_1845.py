from collections import OrderedDict
from sortedcontainers import SortedList, SortedDict, SortedSet

class SeatManager:

    def __init__(self, n: int):
        
        self.seats = SortedDict({i:1 for i in range(1, n+1)})
        self.n = n

    def reserve(self) -> int:
        
        seat = next(iter(self.seats))
        del self.seats[seat]
        
        return seat
      
    
    def unreserve(self, seatNumber: int) -> None:
        self.seats[seatNumber] = 1
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)