class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        length = len(num)
        
        iteration = 0
        
        while iteration < length:
            digit = ord(num[length - 1 - iteration])
            
            if digit % 2 == 1:
                return num[: length - iteration]
            
            iteration += 1
        
        return ""
        