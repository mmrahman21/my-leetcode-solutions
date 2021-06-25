class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges)
        
        next_item = left
        
        for item in ranges:
            a = item[0]
            b = item[1]
            
            while next_item >= a and next_item <= b:
                next_item += 1
                if next_item == right + 1:
                    return True
        return False
            
            
            