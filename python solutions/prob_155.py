class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.head = -1 
        
        
    def push(self, x: int) -> None:
        if len(self.stack) > self.head + 1:
            self.stack[self.head + 1] = x
            
        else:
            self.stack.append(x)
        self.head = self.head + 1
            
    def pop(self) -> None:
        if self.head >=0:
            self.head -= 1
        

    def top(self) -> int:
        if self.head >=0:
            return self.stack[self.head]
        

    def getMin(self) -> int:
        
        if self.head >=0:
            return min(self.stack[ 0 : self.head+1])
           

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()