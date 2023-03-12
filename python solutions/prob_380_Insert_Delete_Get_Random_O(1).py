class RandomizedSet:

    def __init__(self):
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        if not self.dict.pop(val, None):
            self.dict[val] = 1
            return True
        else:
            self.dict[val] = 1
            return False
        

    def remove(self, val: int) -> bool:
        if self.dict.pop(val, None):
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.dict.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()