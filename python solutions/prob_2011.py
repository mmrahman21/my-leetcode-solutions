class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        
        for item in operations:
            if '++' in item:
                X += 1
            else:
                X -= 1
        
        return X
        